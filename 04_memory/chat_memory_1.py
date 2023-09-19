import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  #← ConversationBufferMemoryをインポート
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

memory = ConversationBufferMemory( #← メモリを初期化
    return_messages=True
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="私は会話の文脈を考慮した返答ができるチャットボットです。メッセージを入力してください。").send()

@cl.on_message
async def on_message(message: str):
    memory_message_result = memory.load_memory_variables({}) #← メモリの内容を取得

    messages = memory_message_result['history'] #← メモリの内容からメッセージのみを取得

    messages.append(HumanMessage(content=message)) #← ユーザーからのメッセージを追加

    result = chat( #← Chat modelsを使って言語モデルを呼び出す
        messages
    )

    memory.save_context(  #← メモリにメッセージを追加
        {
            "input": message,  #← ユーザーからのメッセージをinputとして保存
        },
        {
            "output": result.content,  #← AIからのメッセージをoutputとして保存
        }
    )
    await cl.Message(content=result.content).send() #← AIからのメッセージを送信