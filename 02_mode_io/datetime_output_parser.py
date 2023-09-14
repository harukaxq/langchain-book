from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser  #← Output ParserであるDatetimeOutputParserをインポート
from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser() #← DatetimeOutputParserを初期化

chat = ChatOpenAI(model="gpt-3.5-turbo", )

prompt = PromptTemplate.from_template("{product}のリリース日を教えて") #← リリース日を聞く

result = chat(
    [
        HumanMessage(content=prompt.format(product="iPhone8")),  #← iPhone8のリリース日を聞く
        HumanMessage(content=output_parser.get_format_instructions()),  #← output_parser.get_format_instructions()を実行し、言語モデルへの指示を追加する
    ]
)

output = output_parser.parse(result.content) #← 出力結果を解析して日時形式に変換する

print(output)