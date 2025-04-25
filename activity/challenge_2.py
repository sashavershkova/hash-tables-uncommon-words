def uncommon_from_sentences(sentences):
    list_of_sentences_words = []
    for sentence in sentences:
        list_of_sentences_words.extend(set(sentence.split()))

    word_appearance_dict = {}
    for word in list_of_sentences_words:
        word_appearance_dict[word] = word_appearance_dict.get(word, 0) + 1

    uncommon_words_list = []
    for word, count in word_appearance_dict.items():
        if count == 1:
            uncommon_words_list.append(word)

    return uncommon_words_list



# def uncommon_from_sentences(sentences):
#     word_appearance_dict = {}

#     for sentence in sentences:
#         one_sentence_set = set(sentence.split())
#         for word in one_sentence_set:
#             word_appearance_dict[word] = word_appearance_dict.get(word, 0) + 1

#     uncommon_words_list = []
#     for word, count in word_appearance_dict.items():
#         if count == 1:
#             uncommon_words_list.append(word)

#     return uncommon_words_list