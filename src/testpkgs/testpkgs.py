from collections import Counter
from string import punctuation


def load_text(file: str):
    with open(file, "r") as f:
        text = f.read()

    return text


def clean_text(text: str):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(file: str):
    text = load_text(file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)


print(count_words('./zen.txt'))
