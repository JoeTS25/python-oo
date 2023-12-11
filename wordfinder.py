"""Word Finder: finds random words from a dictionary."""
import random
""" Generates random numbers """

class WordFinder:
    def __init__(self, "simple.txt"):
        file = open("simple.txt")
        self.words = self.get_words(file)
        print(f"{len(self.words) words found}")

    def get_words(self, file):
        for word in file:
            return word

    def random_word(self):
        return random.choice(self.words)         

    


