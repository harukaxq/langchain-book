from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI(model="gpt-3.5-turbo")

write_article_chain = LLMChain( #← 記事を書くLLMChainを作成する
    llm=chat,
    prompt=PromptTemplate(
        template="{input}についての記事を書いてください。",
        input_variables=["input"],
    ),
)

translate_chain = LLMChain( #← 翻訳するLLMChainを作成する
    llm=chat,
    prompt=PromptTemplate(
        template="以下の文章を英語に翻訳してください。\n{input}",
        input_variables=["input"],
    ),
)

sequential_chain = SimpleSequentialChain( #← SimpleSequentialChainを作成する
    chains=[ #← 実行するChainを指定する
        write_article_chain,
        translate_chain,
    ]
)

result = sequential_chain.run("エレキギターの選び方")

print(result)