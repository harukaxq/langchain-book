from langchain.chat_models import ChatOpenAI  
from langchain.schema import HumanMessage  

chat = ChatOpenAI(  
    model="gpt-3.5-turbo",  
)

result = chat( 
    [
        HumanMessage(content="茶碗蒸しを作るのに必要な食材を教えて"),
    ]
)
print(result.content)