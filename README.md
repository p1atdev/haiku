# マルコフ連鎖で俳句作るやつ(知らんけど)
まずは必要なやつをpipでインストール
```Shell
pip install markovify
pip install mecab 
```

# 使う
```Shell
python main.py 俳句の元データ.txt
```

｀俳句の元データ.txt`は、生成するための元となるデータです(進次郎構文)
同じディレクトリに`test.txt`として夏目漱石の「吾輩は猫である」を入れてあるので使ってみてください
