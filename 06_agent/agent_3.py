import random  #←ランダムな数字を生成するために必要なモジュールをインポート
from langchain.agents import AgentType, Tool, initialize_agent  #←Toolをインポート
from langchain.chat_models import ChatOpenAI
from langchain.tools import WriteFileTool

chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

tools = [] #← 他のツールは不要なので一旦削除する

tools.append(WriteFileTool( 
    root_dir="./"
))

def min_limit_random_number(min_number): #←最小値を指定できるランダムな数字を生成する関数
    return random.randint(int(min_number), 100000)


tools.append(  #←ツールを追加
    Tool(
        name="Random",  #←ツール名
        description="特定の最小値以上のランダムな数字を生成することができます。",  #←ツールの説明
        func=min_limit_random_number  #←ツールが実行された時に呼び出される関数
    )
)

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  
    verbose=True
)

result = agent.run("10以上のランダムな数字を生成してrandom.txtというファイルに保存してください。")

print(f"実行結果: {result}")
