import os
from nltk import sent_tokenize


train_string = "Как поживаете вы? Как вы, дорогой Дмитрий Сергеич?– спросил его хозяин.– Я очень доволен"
sentences = sent_tokenize(train_string)


def post_processing(str_input):
    from nltk import word_tokenize
    words = word_tokenize(str_input)
    new_words = []
    punctuation = [".", ",", "!", "?"]

    stop_punctuation = [".", "!", "?"]

    for i in words:
        j = i.split(".")
        new_words.extend(j)
    brand_new_words = []
    for i in new_words:
        if i not in punctuation:
            j = " " + i
            brand_new_words.append(j)
        else:
            brand_new_words.append(i)

    new_string = "".join(brand_new_words)
    return new_string


if __name__ == '__main__':
    print(post_processing(train_string))
