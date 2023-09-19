from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import SpacyTextSplitter  #← SpacyTextSplitterをインポート

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(  #← SpacyTextSplitterを初期化する
    chunk_size=300,  #← 分割するサイズを設定
    pipeline="ja_core_news_sm"  #← 分割に使用する言語モデルを設定
)
splitted_documents = text_splitter.split_documents(documents) #← ドキュメントを分割する

print(f"分割前のドキュメント数: {len(documents)}")
print(f"分割後のドキュメント数: {len(splitted_documents)}")
