def rev_word(sentence):

    for word in sentence.split():
        print(word[::-1],end = " ")

sen = "lets start the day"
rev_word(sen)