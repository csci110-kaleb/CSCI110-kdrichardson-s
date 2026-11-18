class HangmanBoard:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.mistakes = 0
        self.max_mistakes = 6

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            return letter in self.word
        self.guessed.add(letter)
        if letter in self.word:
            return True
        self.mistakes += 1
        return False

    def display(self):
        return " ".join(c if c in self.guessed else "_" for c in self.word)

    def is_won(self):
        return "_" not in self.display()

    def is_lost(self):
        return self.mistakes >= self.max_mistakes
