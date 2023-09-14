from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever, RePhraseQueryRetriever #← RePhraseQueryRetrieverをインポートする
from langchain import LLMChain
from langchain.prompts import PromptTemplate

retriever = WikipediaRetriever( 
    lang="ja", 
    doc_content_chars_max=500 
)

llm_chain = LLMChain( #← LLMChainを初期化する
    llm = ChatOpenAI( #← ChatOpenAIを指定する
        temperature = 0
    ), 
    prompt= PromptTemplate( #← PromptTemplateを指定する
        input_variables=["question"],
        template="""以下の質問からWikipediaで検索するべきキーワードを抽出してください。
質問: {question}
"""
))

re_phrase_query_retriever = RePhraseQueryRetriever( #← RePhraseQueryRetrieverを初期化する
    llm_chain=llm_chain, #← LLMChainを指定する
    retriever=retriever, #← WikipediaRetrieverを指定する
)

documents = re_phrase_query_retriever.get_relevant_documents("私はラーメンが好きです。ところでバーボンウイスキーとは何ですか？")

print(documents)