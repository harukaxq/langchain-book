from langchain.prompts import load_prompt

loaded_prompt = load_prompt("prompt.json") #← JSONからPromptTemplateを読み込む

print(loaded_prompt.format(product="iPhone")) #← PromptTemplateを使って文章を生成する