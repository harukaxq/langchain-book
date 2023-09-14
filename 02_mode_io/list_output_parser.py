from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import \
    CommaSeparatedListOutputParser  #← Output ParserであるCommaSeparatedListOutputParserをインポート
from langchain.schema import HumanMessage

output_parser = CommaSeparatedListOutputParser() #← CommaSeparatedListOutputParserを初期化

chat = ChatOpenAI(model="gpt-3.5-turbo", )

result = chat(
    [
        HumanMessage(content="Appleが開発した代表的な製品を3つ教えてください"),
        HumanMessage(content=output_parser.get_format_instructions()),  #← output_parser.get_format_instructions()を実行し、言語モデルへの指示を追加する
    ]
)

output = output_parser.parse(result.content) #← 出力結果を解析してリスト形式に変換する

for item in output: #← リストを一つずつ取り出す
    print("代表的な製品 => " + item)
