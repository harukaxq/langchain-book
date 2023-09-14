from langchain.chat_models import ChatOpenAI  #← ChatOpenAIをインポート
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate  #← PromptTemplateをインポート
from langchain.schema import HumanMessage  #← HumanMessageをインポート
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data", 
    embedding_function=embeddings
)

query = "飛行車の最高速度は？"

documents = database.similarity_search(query)

documents_string = "" #← ドキュメントの内容を格納する変数を初期化

for document in documents:
    documents_string += f"""
---------------------------
{document.page_content}
""" #← ドキュメントの内容を追加

prompt = PromptTemplate( #← PromptTemplateを初期化
    template="""文章を元に質問に答えてください。 

文章: 
{document}

質問: {query}
""",
    input_variables=["document","query"] #← 入力変数を指定
)

chat = ChatOpenAI( #← ChatOpenAIを初期化
    model="gpt-3.5-turbo"
)

result = chat([
    HumanMessage(content=prompt.format(document=documents_string, query=query))
])

print(result.content)
