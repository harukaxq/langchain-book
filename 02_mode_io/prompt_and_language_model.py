from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(  #←クライアントを作成しchatへ保存
    model="gpt-3.5-turbo",  #← 呼び出すモデルを指定
)

prompt = PromptTemplate(  #← PromptTemplateを作成する
    template="{product}はどこの会社が開発した製品ですか？",  #← {product}という変数を含むプロンプトを作成する
    input_variables=[
        "product"  #← productに入力する変数を指定する
    ]
)

result = chat( #← 実行する
    [
        HumanMessage(content=prompt.format(product="iPhone")),
    ]
)
print(result.content)