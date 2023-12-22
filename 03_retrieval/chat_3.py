import os
import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma


embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

chat = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate(template="""文章を元に質問に答えてください。 

文章: 
{document}

質問: {query}
""", input_variables=["document", "query"])

text_splitter = SpacyTextSplitter(chunk_size=300, pipeline="ja_core_news_sm")

@cl.on_chat_start
async def on_chat_start():
    files = None #← ファイルが選択されているか確認する変数

    while files is None: #← ファイルが選択されるまで繰り返す
        files = await cl.AskFileMessage(
            max_size_mb=20,
            content="PDFを選択してください",
            accept=["application/pdf"],
            raise_on_timeout=False,
        ).send()
    file = files[0]

    if not os.path.exists("tmp"): #← tmpディレクトリが存在するか確認
        os.mkdir("tmp") #← 存在しなければ作成する
    with open(f"tmp/{file.name}", "wb") as f: #← PDFファイルを保存する
        f.write(file.content) #← ファイルの内容を書き込む

    documents = PyMuPDFLoader(f"tmp/{file.name}").load() #← 保存したPDFファイルを読み込む
    splitted_documents = text_splitter.split_documents(documents) #← ドキュメントを分割する

    database = Chroma( #← データベースを初期化する
        embedding_function=embeddings,
        # 今回はpersist_directoryを指定しないことでデータベースの永続化を行わない
    )

    database.add_documents(splitted_documents) #← ドキュメントをデータベースに追加する

    cl.user_session.set(  #← データベースをセッションに保存する
        "database",  #← セッションに保存する名前
        database  #← セッションに保存する値
    )

    await cl.Message(content=f"`{file.name}`の読み込みが完了しました。質問を入力してください。").send() #← 読み込み完了を通知する

@cl.on_message
async def on_message(input_message):
    print("入力されたメッセージ: " + input_message)

    database = cl.user_session.get("database") #← セッションからデータベースを取得する

    documents = database.similarity_search(input_message)

    documents_string = ""

    for document in documents:
        documents_string += f"""
    ---------------------------
    {document.page_content}
    """

    result = chat([
        HumanMessage(content=prompt.format(document=documents_string,
                                           query=input_message)) #← input_messageに変更
    ])
    await cl.Message(content=result.content).send()