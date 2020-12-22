import os
import shlex

input_file = "/Users/dmitriosipov/my_research/datasets/tchekhov/tchekhov-train-val/tchekhov_novels.txt"
# ==>
output_file_train_1 = "/Users/dmitriosipov/my_research/deep_learning/text_generation/" \
                      "ru-gpts-telegram/pre-processing/output/tchekhov_train.txt"

output_file_train_2 = "/Users/dmitriosipov/my_research/deep_learning/text_generation/" \
                      "ru-gpts-telegram/pre-processing/output/tchekhov_train_2.txt"

output_file_validation = "/Users/dmitriosipov/my_research/deep_learning/text_generation/" \
                         "ru-gpts-telegram/pre-processing/output/tchekhov_validation.txt"

txt_data = [i.strip() for i in open(input_file).readlines()]

sentences = []
train_size = int(len(txt_data)*0.8)
test_size = int(len(txt_data)*0.9)


def string_processing(str_input):
    import re
    from nltk import word_tokenize
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
    output = re.sub(r'\s\)', ")", pre_output)
    return output




def data_processing(start, end, output_file_name):
    import re
    from nltk import sent_tokenize, word_tokenize
    for i in txt_data[start:end]:
        a = re.sub(r'(\d)+\)(\s)?(\d)+(\s)?-(\s)?[\w\s\(\)]+(\s)?(\<\|n\|\>)', "", i)
        b = a.replace("<|n|>", " ")
        c = re.findall("[^\s]+", b)
        d = " ".join(c)
        m = (d
             .replace("Антон Павлович Чехов", "")
             .replace("Чехов Антон Павлович", "")
             .replace("Антон Чехов", "")
             .replace("А. П. ЧЕХОВ", "")
             .replace("Рассказы", "")
             .replace("  ", "")
             .replace("   ", " ")
             .replace("``", '"')
             .replace("  ", " ")
             .replace("- то", "-то")
             .replace("- c", "-c")
             .replace("- ка", "-ка")
             )
        q = re.sub(r'(\d)+\)\s(\d)+(\s)?', "", m)
        w = re.sub(r'\( ', "(", q)
        j = word_tokenize(str(w))
        with open(output_file_name, 'a') as f:
            if len(j) < 1024:
                f.write(w + "\n")
            elif len(j) < 2048:
                first_batch = j[0:1024]
                second_batch = j[1025:-1]
                first_batch_str = " ".join(first_batch)
                second_batch_str = " ".join(second_batch)
                f.write(string_processing(first_batch_str) + "\n")
                f.write(string_processing(second_batch_str))
            elif len(j) < 3072:
                first_batch = j[0:1024]
                second_batch = j[1025:2048]
                third_batch = j[2049:-1]
                first_batch_str = " ".join(first_batch)
                second_batch_str = " ".join(second_batch)
                third_batch_str = " ".join(third_batch)
                f.write(string_processing(first_batch_str) + "\n")
                f.write(string_processing(second_batch_str) + "\n")
                f.write(string_processing(third_batch_str) + "\n")
            else:
                pass
    return os.system("open " + shlex.quote(output_file_name))


if __name__ == '__main__':
    # print(data_processing(0, 2, output_file_train_1))
    data_processing(0, test_size, output_file_train_1)
    data_processing(test_size, -1, output_file_validation)
    # data_processing(0, -1, output_file_train_2)
