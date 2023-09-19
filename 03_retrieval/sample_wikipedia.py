from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(  #← WikipediaRetrieverを初期化する
    lang="ja",  #← Wikipediaの言語を指定する
)
documents = retriever.get_relevant_documents( #← Wikipediaから関連する記事を取得する
    "大規模言語モデル" #← 検索するキーワードを指定する
)

print(f"検索結果: {len(documents)}件") #← 検索結果の件数を表示する

for document in documents:
    print("---------------取得したメタデータ---------------")
    print(document.metadata) #← メタデータを表示する
    print("---------------取得したテキスト---------------")
    print(document.page_content[:100]) #← テキストの先頭100文字を表示する