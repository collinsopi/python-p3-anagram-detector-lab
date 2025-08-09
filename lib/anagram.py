# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for consistency

    def match(self, words):
        # Sort the letters of the original word for easy comparison
        sorted_word = sorted(self.word)
        
        matches = []
        for w in words:
            # Avoid matching the exact same word
            if w.lower() != self.word and sorted(w.lower()) == sorted_word:
                matches.append(w)
        
        return matches
