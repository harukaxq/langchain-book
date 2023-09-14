from langchain.agents import AgentType, Tool, initialize_agent
from langchain.agents.agent_toolkits import create_retriever_tool  #← create_retriever_toolをインポート
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever #←WikipediaRetrieverをインポート
from langchain.tools import WriteFileTool

chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

tools = [] 

tools.append(WriteFileTool( 
    root_dir="./"
))

retriever = WikipediaRetriever( #←WikipediaRetrieverを初期化
    lang="ja", #←言語を日本語に設定
    doc_content_chars_max=500,  #←記事の最大文字数を500文字に設定
    top_k_results=1 #←検索結果の上位1件を取得
)

tools.append(
    create_retriever_tool(  #←Retrieversを使用するToolを作成
        name="WikipediaRetriever",  #←Toolの名前
        description="受け取った単語に関するWikipediaの記事を取得できる",  #←Toolの説明
        retriever=retriever,  #←Retrieversを指定
    )
)

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  
    verbose=True
)

result = agent.run("スコッチウイスキーについてWikipediaで調べて概要を日本語でresult.txtというファイルに保存してください。")

print(f"実行結果: {result}")