# import markovify
import MeCab
from sys import argv
from os import read
import random


def main():
    file_name = argv[1]
    with open(file_name, "r") as file:
        text = file.read().replace("\n", ".\n")

    # メカブのやつ
    tagger = MeCab.Tagger("-Owakati")
    text = tagger.parse(text)

    words = tagger.parse(text).split(" ")

    length = 0

    # 5,7,5のarray
    fiveWord = []
    sevenWord = []

    longWord = ""

    # テスト用の文章
    testText = "アルプスに日のあるかぎり蕎麦を刈る"
    testText = tagger.parse(testText).split(" ")

    for word in words:
        # for word in testText:
        word = word.replace(".", "")

        length += len(MeCab.Tagger("-Oyomi").parse(word)) - 1

        longWord += word

        # 5 7 5で分類
        if length == 5:
            fiveWord.append(longWord)
            # print(length, ": ", longWord)
        elif length == 7:
            sevenWord.append(longWord)
        elif length > 7:
            length = 0
            longWord = ""

    # 出力する5 7 5
    haiku = [random.choice(fiveWord), random.choice(
        sevenWord), random.choice(fiveWord)]

    # 助詞から始まるやつを除外
    joshi = ["の", "て", "が", "は", "を", "ん", "に", "っ"]

    while (haiku[0][0] in joshi):
        haiku[0][0] = random.choice(fiveWord)

    while (haiku[1][0] in joshi):
        haiku[1][0] = random.choice(fiveWord)

    while (haiku[2][0] in joshi):
        haiku[2][0] = random.choice(fiveWord)

    print(haiku[0], " ", haiku[1], " ", haiku[2])

    # print(fiveWord)

    # print(text)

    # # マルコフ連鎖
    # sentence = None
    # while (sentence == None or len(sentence) > 500):
    #     model = markovify.Text(text, state_size=1)
    #     sentence = model.make_sentence(max=20)

    # print(sentence.replace(" ", "").replace(".", "\n"))


if __name__ == "__main__":
    main()
