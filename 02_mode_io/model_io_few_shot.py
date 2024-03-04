from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "LangChainはChatGPT・Large Language Model (LLM)の実利用をより柔軟に簡易に行うためのツール群です",  #← 入力例
        "output": "LangChainは、ChatGPT・Large Language Model (LLM)の実利用をより柔軟に、簡易に行うためのツール群です。"  #← 出力例
    }
]

prompt = PromptTemplate(  #← PromptTemplateの準備
    input_variables=["input", "output"],  #← inputとoutputを入力変数として設定
    template="入力: {input}\n出力: {output}",  #← テンプレート
)

few_shot_prompt = FewShotPromptTemplate(  #← FewShotPromptTemplateの準備
    examples=examples,  #← 入力例と出力例を定義
    example_prompt=prompt,  #← FewShotPromptTemplateにPromptTemplateを渡す
    prefix="以下の句読点の抜けた入力に句読点を追加してください。追加して良い句読点は「、」「。」のみです。他の句読点は追加しないでください。",  #← 指示を追加する
    suffix="入力: {input_string}\n出力:",  #← 出力例の入力変数を定義
    input_variables=["input_string"],  #← FewShotPromptTemplateの入力変数を設定
)
llm = OpenAI(
    model="gpt-3.5-turbo-instruct"
)
formatted_prompt = few_shot_prompt.format( #← FewShotPromptTemplateを使ってプロンプトを作成
    input_string="私はさまざまな機能がモジュールとして提供されているLangChainを使ってアプリケーションを開発しています"
)
result = llm.predict(formatted_prompt)
print("formatted_prompt: ", formatted_prompt)
print("result: ", result)