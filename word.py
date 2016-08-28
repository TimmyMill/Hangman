import random


class Word:

    # words

    def __init__(self):
        self.words = []
        #,file = open("word_list.txt", 'r')

    # file = open("word_list.txt", 'r')

    def read_file(self, file):

        while True:
            inline = file.readline()
            if inline == '':
                break
            else:
                file.words.append(inline)
        return words

    def select_word(self):
        wordlist = []
        for w in wordlist:
            w = w.split(";")
            wordlist.append(w)

        random.shuffle(wordlist)

        return wordlist[0]
