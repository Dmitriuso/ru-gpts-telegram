from nltk import sent_tokenize


train_string = "Как поживаете вы? Как вы, дорогой Дмитрий Сергеич?– спросил его хозяин. – Я очень доволен"
sentences = sent_tokenize(train_string)


def post_processing(str_input):
    import re
    from nltk import word_tokenize, sent_tokenize
    words = word_tokenize(str_input)
    new_words = []
    punctuation = [".", ",", "!", "?", ";", ":"]
    for i in words:
        if i not in punctuation:
            j = " " + i
            new_words.append(j)
        else:
            new_words.append(i)
    new_string = "".join(new_words)
    new_clean_string = (new_string
                        .replace("  ", " ")
                        .replace("   ", " ")
                        .replace("``", '"')
                        .replace("- то", "-то")
                        .replace("- с", "-с")
                        .replace("- ка", "-ка")
                        )
    pre_output = re.sub(r'\( ', "(", new_clean_string)
    output_string = re.sub(r'\s\)', ")", pre_output)
    output_phrases = sent_tokenize(output_string)
    print(output_phrases)
    return " ".join(output_phrases[0:-1])


if __name__ == '__main__':
    print(post_processing(train_string))
