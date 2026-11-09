#the first fucntion stores what you guess and how many mistakes you have and also the word you want the player to guess.
class HangmanBoard:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.mistakes = 0
#This function says that if the letter you guessed is in the word add it to the display and if the letter is wrong add +1 to the mistakes tally.
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            return
        self.guessed.add(letter)
        if letter not in self.word:
            self.mistakes += 1
#This displays the word as dashes and adds whatever correct letters you guess over the course of the game.
    def display(self):
        return " ".join(c if c in self.guessed else "_" for c in self.word)
