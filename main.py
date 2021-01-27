from os import read
from sys import argv
# from janome.tokenizer import Tokenizer
import MeCab
import markovify


def main():
    file_name = argv[1]
    with open(file_name, "r") as file:
        text = file.read().replace("\n", ".\n")

    # メカブのやつ
    tagger = MeCab.Tagger("-Owakati")
    text = tagger.parse(text)

    # print(text)

    # マルコフ連鎖
    sentence = None
    while (sentence == None or len(sentence) > 2000):
        model = markovify.Text(text, state_size=1)
        sentence = model.make_sentence(max=10)

    print(sentence.replace(" ", "").replace(".", "\n"))


if __name__ == "__main__":
    main()
