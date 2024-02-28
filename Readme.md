# LangChain Book

このリポジトリは書籍「[LangChain 完全入門　生成 AI アプリケーション開発がはかどる大規模言語モデルの操り方](https://book.impress.co.jp/books/1123101047)」で作成するソースコードです。

## サンプルコードが正常に動作しない問題について

### ライブラリバージョンについて

本書のサンプルコードで使用しているライブラリに破壊的変更があり、手順どおりにコマンドを実行すると正常動作しないバージョンのライブラリがインストールされる事象が確認されています。

以下の手順でライブラリをインストールしてください。

・Windows の場合

```
wget https://raw.githubusercontent.com/harukaxq/langchain-book/master/requirements.txt -OutFile requirements.txt
python3 -m pip install -r requirements.txt
```

・macOS の場合

```
wget https://raw.githubusercontent.com/harukaxq/langchain-book/master/requirements.txt
python3 -m pip install -r requirements.txt
```

### Python のバージョンについて

3.12 以上のバージョンを使用すると、サンプルコードが正常に動作しない事象が確認されています。3.10、3.11 で動作確認しているため、正常に動作しない場合は、Python のバージョンを 3.10 以上、3.12 未満に変更してください。

### ソースコードの誤りについて
124ページ、chat_3.pyの80行目に誤りがあり、正常に動作しません。以下のように修正してください。


誤：

```python
result = chat([
    HumanMessage(content=prompt.format(documents=documents_string,
                                       query=input_message)) #← input_messageに変更
])
```

正：

```python
result = chat([
    HumanMessage(content=prompt.format(document=documents_string,
                                       query=input_message)) #← input_messageに変更
])
```

formatメソッドでの引数名はdocumentsではなくdocumentが正しいです。

### Agentモジュールで使用するモデルについて
Agentを動作させるためのモデルとして、gpt-3.5-turboを使用するとプロンプトを無視してしまい、正常に動作しない問題が確認されています。

執筆当初は性能の良いモデルである、gpt-4を使用するにはOpenAIに申請が必要な都合上、gpt-3.5-turboを使用していましたが、現在は全員に開放されています。

gpt-3.5-turboを使用すると正常に動作しない場合は、以下のように修正してgpt-4を使用してください。

```python
chat = ChatOpenAI( temperature=0, model="gpt-3.5-turbo" )
```
↓
```python
chat = ChatOpenAI( temperature=0, model="gpt-4" )
```