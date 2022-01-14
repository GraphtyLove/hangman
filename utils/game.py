import random

class Hangman():
    possible_words = {'becode', 'learning', 'mathematics', 'sessions'}
    word_to_find = "" # each element is a letter of the word to find
    lives = 5
    correctly_guessed_letters = list()
    wrongly_guessed_letters = set() 
    turn_count = 0

    @staticmethod
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def __init__(self):
        self.word_to_find = random.sample(self.possible_words, 1)[0]
        self.correctly_guessed_letters = ['_',] * len(self.word_to_find)
        
    def play(self, c):
        c = c.lower()
        if not 'a' <= c <= 'z':
            print(F"{c} is not a letter")
            return

        l = self.find(self.word_to_find, c)
        if l:
            for i in l:
                self.correctly_guessed_letters[i] = c
        else:
            self.wrongly_guessed_letters.add(c)
            self.lives -= 1

        self.turn_count += 1

    def well_played(self):
        print(F"You found the word: {self.word_to_find} with {self.lives} lives to spare!")

    def game_over(self):
        print("Game over!")
    
    def start_game(self):
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self.play(input('What is your guess? Character: '))
            print(self)

        if self.lives == 0:
            self.game_over()
        elif '_' not in self.correctly_guessed_letters:
            self.well_played()
        else:
            print("Houston, we have a problem!")

    def __str__(self):
        return F"Guessed: {''.join(self.correctly_guessed_letters)}, {self.lives} lives remaining."

    

            

            

