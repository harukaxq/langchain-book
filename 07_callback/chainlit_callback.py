import chainlit as cl
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    temperature=0,  
    model="gpt-3.5-turbo"
)

tools = load_tools( 
    [
        "serpapi",
    ]
)

agent = initialize_agent(tools=tools, llm=chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Agentの初期化が完了しました").send() 

@cl.on_message
async def on_message(input_message):
    result = agent.run( #← Agentを実行する
        input_message, #← 入力メッセージ
        callbacks=[ #← コールバックを指定
            cl.LangchainCallbackHandler() #← chainlitに用意されているCallbacksを指定
        ]
    )
    await cl.Message(content=result).send()
