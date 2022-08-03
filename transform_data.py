def transform_text_into_words(text: str) -> list:
    words_2d = []
    for i in text:
        words_2d.append(i.split())
    words = sum(words_2d, [])
    return words


def clean_string(text: str) -> str:
    text = re.split(' |:|\.|\(|\)|,|"|;|/|\n|\t|-|\?|\[|\]|!', text)
    text = ' '.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords_list])
    return text


def string_to_normal_form(string_def):
    string_temp = string_def.split()
    for i in tqdm(range(len(string_temp))):
        string_temp[i] = morph.parse(string_temp[i])[0].normal_form
        # if (string_lst[i] == 'аду'):
        #     string_lst[i] = 'ад'
        # if (string_lst[i] == 'рая'):
        #     string_lst[i] = 'рай'
    string_def = ' '.join(string_temp)
    return string_def
