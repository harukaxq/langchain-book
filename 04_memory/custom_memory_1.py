import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory  # ConversationBufferWindowMemoryをインポート

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

memory = ConversationBufferWindowMemory(
    return_messages=True,
    k=3 # 3往復分のメッセージを記憶する
)

chain = ConversationChain(
    memory=memory,
    llm=chat,
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="私は会話の文脈を考慮した返答ができるチャットボットです。メッセージを入力してください。").send()

@cl.on_message
async def on_message(message: str):
    messages = chain.memory.load_memory_variables({})["history"] # 保存されているメッセージを取得する

    print(f"保存されているメッセージの数: {len(messages)}" # 保存されているメッセージの数を表示する
          )

    for saved_message in messages: # 保存されているメッセージを1つずつ取り出す
        print(saved_message.content # 保存されているメッセージを表示する
              )

    result = chain(message)

    await cl.Message(content=result["response"]).send()