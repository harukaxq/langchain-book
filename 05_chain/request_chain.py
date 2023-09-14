from langchain.chains import LLMChain, LLMRequestsChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI()

prompt = PromptTemplate( #← PromptTemplateを初期化
    input_variables=["query",
                     "requests_result"],
    template="""以下の文章を元に質問に答えてください。
文章: {requests_result}
質問: {query}""",
)

llm_chain = LLMChain(
    llm=chat,
    prompt=prompt,
    verbose=True,
)

chain = LLMRequestsChain(  #← LLMRequestsChainを初期化
    llm_chain=llm_chain,  #← llm_chainにはLLMChainを指定
)

print(chain({
    "query": "東京の天気について教えて",
    "url": "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json",
}))