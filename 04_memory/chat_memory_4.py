import os
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

@cl.on_chat_start
async def on_chat_start():
    thread_id = None
    while not thread_id: #← スレッドIDが入力されるまで繰り返す
        res = await cl.AskUserMessage(content="私は会話の文脈を考慮した返答ができるチャットボットです。スレッドIDを入力してください。", timeout=600).send() #← AskUserMessageを使ってスレッドIDを入力
        if res:
            thread_id = res['content']

    history = RedisChatMessageHistory(  #← 新しくチャットが始まるたびに初期化するようにon_chat_startに移動
        session_id=thread_id,  #← スレッドIDをセッションIDとして指定
        url=os.environ.get("REDIS_URL"),
    )

    memory = ConversationBufferMemory( #← 新しくチャットが始まるたびに初期化するようにon_chat_startに移動
        return_messages=True,
        chat_memory=history,
    )

    chain = ConversationChain( #← 新しくチャットが始まるたびに初期化するようにon_chat_startに移動
        memory=memory,
        llm=chat,
    )

    memory_message_result = chain.memory.load_memory_variables({}) #← メモリの内容を取得

    messages = memory_message_result['history']

    for message in messages:
        if isinstance(message, HumanMessage): #← ユーザーからのメッセージかどうかを判定
            await cl.Message( #← ユーザーからのメッセージの場合はauthorUserを指定して送信
                author="User",
                content=f"{message.content}",
            ).send()
        else:
            await cl.Message( #← AIからのメッセージの場合はChatBotを指定して送信
                author="ChatBot",
                content=f"{message.content}",
            ).send()
    cl.user_session.set("chain", chain) #← 履歴をセッションに保存

@cl.on_message
async def on_message(message: str):
    chain = cl.user_session.get("chain") #← セッションから履歴を取得

    result = chain(message)

    await cl.Message(content=result["response"]).send()