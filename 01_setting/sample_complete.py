import json
import openai

response = openai.Completion.create(  #←ChatCompletionではなく、Completionを使っている
    engine="gpt-3.5-turbo-instruct",  #←modelではなくengineを指定し、gpt-3.5-turbo-instructを指定
    prompt="今日の天気がとても良くて、気分が",  #←promptを指定
    stop="。",  #←文字が出現したら文章を終了する
    max_tokens=100,  #←最大のトークン数
    n=2,  #←生成する文章の数
    temperature=0.5  #←多様性を表すパラメータ
)

print(json.dumps(response, indent=2, ensure_ascii=False))
