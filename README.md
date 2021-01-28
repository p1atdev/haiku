# ~~マルコフ連鎖で~~俳句作るやつ

まずは必要なやつを pip でインストール
環境によっては pip の代わりに pip3 を使うこともあるよ!

```Shell
pip install markovify
pip install mecab
```

# 使う

```Shell
python main.py 俳句の元データ.txt
```

`俳句の元データ.txt`は、生成するための元となるデータです(進次郎構文) 同じディレクトリに`test.txt`として夏目漱石の「吾輩は猫である」を入れてあるので使ってみてください
