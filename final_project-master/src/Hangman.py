import pygame
import os

class Hangman():
    def __init__(self):
        '''
        Initializes the hangman object
        args:
        lives (int) - the number of lives that the player has, this starts at 0
        assets_folder (str) - a string that helps path to the assets folder with all the images
        hangman_stages (list) - a list of the nine hangman stages
        '''
        self.lives = 0
        
        assets_folder = os.path.join(os.path.dirname(__file__), '..', 'assets')
        self.hangman_stages = [
            os.path.join(assets_folder, "hangman_one.png"), 
            os.path.join(assets_folder, "hangman_two.png"), 
            os.path.join(assets_folder, "hangman_three.png"), 
            os.path.join(assets_folder, "hangman_four.png"), 
            os.path.join(assets_folder, "hangman_five.png"), 
            os.path.join(assets_folder, "hangman_six.png"), 
            os.path.join(assets_folder, "hangman_seven.png"), 
            os.path.join(assets_folder, "hangman_eight.png"), 
            os.path.join(assets_folder, "hangman_nine.png")
        ]

    def get_hangman_stage(self):
        '''
        returns the hangman stage depending on the number of lives remaining
        return: 
        returns lives as hangman stages
        '''
        return self.hangman_stages[self.lives]
    
    def update_lives(self):
        '''
        increases the number of lives depending on the number of incorrect guesses made
        '''
        if self.lives < len(self.hangman_stages) - 1:
            self.lives += 1