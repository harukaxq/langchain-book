from langchain.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("./sample.pdf") #← sample.pdfを読み込む
documents = loader.load()

print(f"ドキュメントの数: {len(documents)}") #← ドキュメントの数を確認する
print(f"1つめのドキュメントの内容: {documents[0].page_content}") #← 1つめのドキュメントの内容を確認する
print(f"1つめのドキュメントのメタデータ: {documents[0].metadata}") #← 1つめのドキュメントのメタデータを確認する
