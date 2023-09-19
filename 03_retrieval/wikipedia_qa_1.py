from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI()

retriever = WikipediaRetriever(  #← WikipediaRetrieverを初期化する
    lang="ja",  #← Wikipediaの言語を指定する
    doc_content_chars_max=500,  #← 取得するテキストの最大文字数を指定する
    top_k_results=2,  #← 検索結果の上位何件を取得するかを指定する
)

chain = RetrievalQA.from_llm( #← RetrievalQAを初期化する
    llm=chat, #← 使用するChat modelsを指定する
    retriever=retriever, #← 使用するRetrieverを指定する
    return_source_documents=True, #← 情報の取得元のドキュメントを返すようにする
)

result = chain("バーボンウイスキーとは？") #← RetrievalQAを実行する

source_documents = result["source_documents"] #← 情報の取得元のドキュメントを取得する

print(f"検索結果: {len(source_documents)}件") #← 検索結果の件数を表示する
for document in source_documents:
    print("---------------取得したメタデータ---------------")
    print(document.metadata)
    print("---------------取得したテキスト---------------")
    print(document.page_content[:100])
print("---------------返答---------------")
print(result["result"]) #← 返答を表示する