from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,  #← streamingをTrueに設定し、ストリーミングモードで実行
    callbacks=[
        StreamingStdOutCallbackHandler()  #← StreamingStdOutCallbackHandlerをコールバックとして設定
    ]
)
resp = chat([ #← リクエストを送信
    HumanMessage(content="おいしいステーキの焼き方を教えて")
])