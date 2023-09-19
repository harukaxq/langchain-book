from langchain.callbacks.base import BaseCallbackHandler #← BaseCallbackHandlerをインポート
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


class LogCallbackHandler(BaseCallbackHandler): #← Callbackを作成する

    def on_chat_model_start(self, serialized, messages, **kwargs): #← Chat modelsの実行開始時に呼び出される処理を定義する
        print("Chat modelsの実行を開始します....")
        print(f"入力: {messages}")

    def on_chain_start(self, serialized, inputs, **kwargs): #← Chainの実行開始時に呼び出される処理を定義する
        print("Chainの実行を開始します....")
        print(f"入力: {inputs}")

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    callbacks=[ #← Chat modelsの初期化時にCallbackを指定する
        LogCallbackHandler() #← 作成したLogCallbackHandlerを指定する
    ]
)

result = chat([
    HumanMessage(content="こんにちは！"),
])

print(result.content)