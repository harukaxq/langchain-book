from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings  #← OpenAIEmbeddingsをインポート
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma  #← Chromaをインポート

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300, 
    pipeline="ja_core_news_sm"
)
splitted_documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings( #← OpenAIEmbeddingsを初期化する
    model="text-embedding-ada-002" #← モデル名を指定
)

database = Chroma(  #← Chromaを初期化する
    persist_directory="./.data",  #← 永続化データの保存先を指定
    embedding_function=embeddings  #← ベクトル化するためのモデルを指定
)

database.add_documents(  #← ドキュメントをデータベースに追加
    splitted_documents,  #← 追加するドキュメント
)

print("データベースの作成が完了しました。") #← 完了を通知する