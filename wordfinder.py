"""Word Finder: finds random words from a dictionary."""

import random 

import parser

class WordFinder:
    

    def __init__(self, txt):

        text = open(txt)
        self.words = self.parse(text)
        print(f"{len(self.words)} words read")

    def parse(self, text):
        

        return [w.strip() for w in text]

    def random(self):
        

        return random.choice(self.words)