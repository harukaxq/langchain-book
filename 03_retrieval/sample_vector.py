from langchain.embeddings import OpenAIEmbeddings  #← OpenAIEmbeddingsをインポート
from numpy import dot  #← ベクトルの類似度を計算するためにdotをインポート
from numpy.linalg import norm  #← ベクトルの類似度を計算するためにnormをインポート

embeddings = OpenAIEmbeddings( #← OpenAIEmbeddingsを初期化する
    model="text-embedding-ada-002"
)

query_vector = embeddings.embed_query("飛行車の最高速度は？") #← 質問をベクトル化

print(f"ベクトル化された質問: {query_vector[:5]}") #← ベクトルの一部を表示

document_1_vector = embeddings.embed_query("飛行車の最高速度は時速150キロメートルです。") #← ドキュメント1のベクトルを取得
document_2_vector = embeddings.embed_query("鶏肉を適切に下味をつけた後、中火で焼きながらたまに裏返し、外側は香ばしく中は柔らかく仕上げる。") #← ドキュメント2のベクトルを取得

cos_sim_1 = dot(query_vector, document_1_vector) / (norm(query_vector) * norm(document_1_vector)) #← ベクトルの類似度を計算
print(f"ドキュメント1と質問の類似度: {cos_sim_1}")
cos_sim_2 = dot(query_vector, document_2_vector) / (norm(query_vector) * norm(document_2_vector)) #← ベクトルの類似度を計算
print(f"ドキュメント2と質問の類似度: {cos_sim_2}")