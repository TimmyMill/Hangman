import random


class Words:

    def __init__(self):
        self.wordlist = []

    def read_file(self):

        file = open("word_list.txt", 'r')

        while True:
            inline = file.readline()
            if inline == '':
                break
            else:
                self.wordlist.append(inline)

        file.close()

        return self.wordlist

    def select_word(self):
        self.read_file()
        wordlist = self.wordlist
        random.shuffle(wordlist)

        return wordlist[0]

    def print_word(self):
        word = self.select_word()
        print(word)
