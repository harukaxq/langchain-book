from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI()

memory = ConversationBufferMemory(return_messages=True)

chain = ConversationChain( #← ConversationChainを初期化
    memory=memory, #← Memoryモジュールを指定
    llm=chat, #← 言語モデルを指定
)