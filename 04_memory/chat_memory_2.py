import chainlit as cl
from langchain.chains import ConversationChain  #← ConversationChainを追加
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

memory = ConversationBufferMemory( 
    return_messages=True
)

chain = ConversationChain( #← ConversationChainを初期化
    memory=memory,
    llm=chat,
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="私は会話の文脈を考慮した返答をできるチャットボットです。メッセージを入力してください。").send()

@cl.on_message
async def on_message(message: str):

    result = chain( #← ConversationChainを使って言語モデルを呼び出す
        message #← ユーザーからのメッセージを引数に指定
    )

    await cl.Message(content=result["response"]).send()