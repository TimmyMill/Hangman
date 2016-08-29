import random


class Words:

    def __init__(self):
        self.wordlist = []

    def read_file(self):

        # opens a text file using "read mode"
        file = open("word_list.txt", 'rt')

        # reads in each line from the text file
        while True:
            inline = file.readline()
            if inline == '':  # loops until there are no more lines to read
                break

            else:
                self.wordlist.append(inline)  # adds each line to the end of our word list

        file.close()

        return self.wordlist

    def create_wordlist(self):
        # if the list's length is 0, we need to populate it
        if len(self.wordlist) == 0:

            self.read_file()
            random.shuffle(self.wordlist)

    def select_word(self):
        self.create_wordlist()
        return self.wordlist[0]

    def print_word(self):
        word = self.select_word()
        print(word)
