import random
from src.Hangman import Hangman

class Guessing:
    def __init__(self, word_list):
        '''
        initializes the guessing game
        args:
        word_list (list) - this is a list of random words
        '''
        self.word = random.choice(word_list)
        self.correct_letters = set()
        self.incorrect_letters = set()
        self.hangman = Hangman()
        
    def guess(self, letter):
        '''
        takes in a guess from the player and sorts it into the correct or wrong choices
        args:
        letter (str) - letter is the letter guessed by the player
        '''
        if letter in self.word:
            self.correct_letters.add(letter)
        else:
            self.incorrect_letters.add(letter)
            self.hangman.update_lives()
    
    def display_word(self):
        '''
        displays the word with "_" if the letter hasn't been guessed and the letter if the letter is guessed correctly
        return:
        returns the word with progress
        '''
        return " ".join([letter if letter in self.correct_letters else "_" for letter in self.word])
    
    def is_win(self):
        '''
        determines whether the player has won the game
        return:
        returns the all letters have been guessed
        '''
        return all(letter in self.correct_letters for letter in self.word)

    def is_game_over(self, hangman_stages):
        '''
        determines whether the player has lost the game
        return:
        returns all lives have been lost
        '''
        return self.hangman.lives >= len(self.hangman.hangman_stages) - 1

    def get_result_message(self):
        '''
        determines the message depending on the result of the game
        return:
        returns a message if the game is over
        '''
        if self.is_win():
            return "You Win!"
        elif self.is_game_over(self.hangman.hangman_stages):
            return f"You Lose! The word was: {self.word}"