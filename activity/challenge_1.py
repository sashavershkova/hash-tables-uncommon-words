def uncommon_from_sentences(sentences):
    big_sentence = " ".join(sentences)

    counter_dict = {}
    for word in big_sentence.split():
        counter_dict[word] = counter_dict.get(word, 0) + 1
    
    uncommon_list = []
    for word, counter in counter_dict.items():
        if counter == 1:
            uncommon_list.append(word)
    
    return uncommon_list