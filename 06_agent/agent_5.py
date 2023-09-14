from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  #←ConversationBufferMemoryをインポート
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

tools = []

# WriteFileToolを削除

retriever = WikipediaRetriever(
    lang="ja",
    doc_content_chars_max=500,
    top_k_results=1
)

tools.append(
    create_retriever_tool(  #←Retrieversを使用するToolを作成
        name="WikipediaRetriever",  #←Toolの名前
        description="受け取った単語に関するWikipediaの記事を取得できる",  #←Toolの説明
        retriever=retriever,  #←Retrieversを指定
    )
)

memory = ConversationBufferMemory(  #←ConversationBufferMemoryを初期化
    memory_key="chat_history",  #←メモリのキーを設定
    return_messages=True  #←メッセージを返すように設定
)

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,  #←Agentのタイプを対話できるように変更
    memory=memory,  #←Memoryを指定
    verbose=True
)

result = agent.run("スコッチウイスキーについてWikipediaで調べて日本語で概要をまとめてください。") #←Wikipediaで調べるように指示
print(f"1回目の実行結果: {result}") #←実行結果を表示
result_2 = agent.run("以前の指示をもう一度実行してください。") #←以前の指示をもう一度実行するように指示
print(f"2回目の実行結果: {result_2}") #←実行結果を表示
