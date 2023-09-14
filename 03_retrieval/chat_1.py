import chainlit as cl


@cl.on_chat_start #← チャットが開始されたときに実行される関数を定義する
async def on_chat_start():
    await cl.Message(content="準備ができました！メッセージを入力してください！").send() #← 初期表示されるメッセージを送信する

@cl.on_message #← メッセージが送信されたときに実行される関数を定義する
async def on_message(input_message):
    print("入力されたメッセージ: " + input_message)
    await cl.Message(content="こんにちは!").send() #← チャットボットからの返答を送信する