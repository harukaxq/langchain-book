from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, validator

chat = ChatOpenAI()

class Smartphone(BaseModel): #← Pydanticのモデルを定義する
    release_date: str = Field(description="スマートフォンの発売日") #← Fieldを使って説明を追加する
    screen_inches: float = Field(description="スマートフォンの画面サイズ(インチ)")
    os_installed: str = Field(description="スマートフォンにインストールされているOS")
    model_name: str = Field(description="スマートフォンのモデル名")

    @validator("screen_inches") #← validatorを使って値を検証する
    def validate_screen_inches(cls, field): #← validatorの引数には、検証するフィールドと値が渡される
        if field <= 0: #← screen_inchesが0以下の場合はエラーを返す
            raise ValueError("Screen inches must be a positive number")
        return field

parser = PydanticOutputParser(pydantic_object=Smartphone) #← PydanticOutputParserをSmartPhoneモデルで初期化する

result = chat([ #← Chat modelsにHumanMessageを渡して、文章を生成する
    HumanMessage(content="Androidでリリースしたスマートフォンを1個挙げて"),
    HumanMessage(content=parser.get_format_instructions())
])

parsed_result = parser.parse(result.content) #← PydanticOutputParserを使って、文章をパースする

print(f"モデル名: {parsed_result.model_name}")