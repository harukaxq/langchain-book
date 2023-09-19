from langchain.prompts import PromptTemplate

prompt = PromptTemplate(template="{product}はどこの会社が開発した製品ですか？", input_variables=["product"])
prompt_json = prompt.save("prompt.json") #← PromptTemplateをJSONに変換する
