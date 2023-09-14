from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import OutputFixingParser  #←OutputFixingParserを追加
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, validator

chat = ChatOpenAI()

class Smartphone(BaseModel):
    release_date: str = Field(description="スマートフォンの発売日")
    screen_inches: float = Field(description="スマートフォンの画面サイズ(インチ)")
    os_installed: str = Field(description="スマートフォンにインストールされているOS")
    model_name: str = Field(description="スマートフォンのモデル名")

    @validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("Screen inches must be a positive number")
        return field


parser = OutputFixingParser.from_llm(  #← OutputFixingParserを使用するように書き換え
    parser=PydanticOutputParser(pydantic_object=Smartphone),  #← parserを設定
    llm=chat  #← 修正に使用する言語モデルを設定
)

result = chat([HumanMessage(content="Androidでリリースしたスマートフォンを1個挙げて"), HumanMessage(content=parser.get_format_instructions())])

parsed_result = parser.parse(result.content)

print(f"モデル名: {parsed_result.model_name}")
print(f"画面サイズ: {parsed_result.screen_inches}インチ")
print(f"OS: {parsed_result.os_installed}")
print(f"スマートフォンの発売日: {parsed_result.release_date}")