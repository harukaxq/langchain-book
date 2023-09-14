from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    temperature=0,  #← temperatureを0に設定して出力の多様性を抑える
    model="gpt-3.5-turbo"
)

tools = load_tools(  #← LangChainに用意されているToolを読み込む
    [
        "requests",  #← 特定のURLの結果を取得できるToolであるrequestsを読み込む
    ]
)

agent = initialize_agent(  #← Agentを初期化する
    tools=tools,  #← Agentが使用することができるToolの配列を設定
    llm=chat,  #← Agentが使用する言語モデルを指定
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,  #←ReAct方式で動作するように設定する
    verbose=True  #← 実行途中のログを表示する
)

result = agent.run("""以下のURLにアクセスして東京の天気を調べて日本語で答えてください。
https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json
""")

print(f"実行結果: {result}")