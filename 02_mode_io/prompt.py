from langchain import PromptTemplate  #← PromptTemplateをインポート

prompt = PromptTemplate(  #← PromptTemplateを初期化する
    template="{product}はどこの会社が開発した製品ですか？",  #← {product}という変数を含むプロンプトを作成する
    input_variables=[
        "product"  #← productに入力する変数を指定する
    ]
)

print(prompt.format(product="iPhone"))
print(prompt.format(product="Xperia"))