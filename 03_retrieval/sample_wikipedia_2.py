from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever( 
    lang="ja", 
    doc_content_chars_max=100,
    top_k_results=1
)
documents = retriever.get_relevant_documents( 
    "私はラーメンが好きです。ところでバーボンウイスキーとは何ですか？" 
)
print(documents)