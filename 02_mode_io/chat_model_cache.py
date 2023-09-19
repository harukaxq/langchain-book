import time  #← 実行時間を計測するためにtimeモジュールをインポート
import langchain
from langchain.cache import InMemoryCache  #← InMemoryCacheをインポート
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache() #← llm_cacheにInMemoryCacheを設定

chat = ChatOpenAI()
start = time.time() #← 実行開始時間を記録
result = chat([ #← 一度目の実行を行う
    HumanMessage(content="こんにちは！")
])

end = time.time() #← 実行終了時間を記録
print(result.content)
print(f"実行時間: {end - start}秒")

start = time.time() #← 実行開始時間を記録
result = chat([ #← 同じ内容で二度目の実行を行うことでキャッシュが利用され、即時に実行完了している
    HumanMessage(content="こんにちは！")
])

end = time.time() #← 実行終了時間を記録
print(result.content)
print(f"実行時間: {end - start}秒")