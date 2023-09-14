from langchain.chat_models import ChatOpenAI  #← モジュールをインポート
from langchain.schema import HumanMessage  #← ユーザーからのメッセージであるHumanMessageをインポート

chat = ChatOpenAI(  #←クライアントを作成しchatへ保存
    model="gpt-3.5-turbo",  #← 呼び出すモデルを指定
)

result = chat( #← 実行する
    [
        HumanMessage(content="こんにちは！"),
    ]
)
print(result.content)
