from langchain.agents import AgentType, initialize_agent, load_tools  #←load_toolsをインポートを追加
from langchain.chat_models import ChatOpenAI
from langchain.tools.file_management import WriteFileTool  #←ファイル書き込みできるToolをインポート

chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

tools = load_tools(
    [
        "requests_get",
        "serpapi" #←serpapiを追加
    ],
    llm=chat
)

tools.append(WriteFileTool( #←ファイル書き込みできるToolを追加
    root_dir="./"
))

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  #←Agentのタイプを変更
    verbose=True
)

result = agent.run("北海道の名産品を調べて日本語でresult.txtというファイルに保存してください。") #←実行結果をファイルに保存するように指示

print(f"実行結果: {result}")