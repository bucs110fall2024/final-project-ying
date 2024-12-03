import pygame
import string
import requests
from src.Guessing import Guessing
from src.Hangman import Hangman
from src.Used_letters import Used_Letters

class Controller:
    def __init__(self):
        """
        Inilializes the hangman game
        args:
        WIDTH, HEIGHT (int) - dimensions of the game window
        screen (Surface) - pygame screen object
        FONT, SMALL_FONT (pygame.Font) - size of fonts for text
        WHITE, BLACK, RED (tuple) - colors in their numerical form
        word_list (list) - list of words for the game generated from the cat fact API
        """        
        self.WIDTH = 600
        self.HEIGHT = 400
        self.FONT_SIZE = 32
        self.SMALL_FONT_SIZE = 24
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        
        url = "https://meowfacts.herokuapp.com/"

        response = requests.get(url).json()
        fact = response.get('data', [])[0]
        words = fact.split()
        self.word_list = [word.upper() for word in words]
        
        pygame.init()
        
        self.FONT = pygame.font.SysFont("Comic Sans", self.FONT_SIZE)
        self.SMALL_FONT = pygame.font.SysFont("Comic Sans", self.SMALL_FONT_SIZE)
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Hangman Game")
        
        self.in_menu = True
        
    def main_loop(self):
        '''
        runs the game through each phase (start menu, game menu)
        args:
        event (var) - event determines when there is an input through a keyboard
        in_menu (var) - a boolean value determining whether the user is in the menu interface or not
        '''
        while self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.handle_menu_input(event)
            self.draw_start_menu()
        
        while not self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.handle_game_input(event)
            self.draw_game()
            pygame.display.update()
            
    def draw_start_menu(self):
        '''
        draws a start menu with the options to start or quit the game
        args:
        title_text (Surface) - the text that identifies the game as Hangman Game in the game display
        start_text (Surface) - the text that tells the player to press ENTER to Start the game in the game display
        quit_text (Surface) - the text that tells the player to press ESC to Quit the game in the game display
        '''
        self.screen.fill(self.WHITE)

        title_text = self.FONT.render("Hangman Game", True, self.BLACK)
        self.screen.blit(title_text, (self.WIDTH // 2 - title_text.get_width() // 2, self.HEIGHT // 3))

        start_text = self.SMALL_FONT.render("Press ENTER to Start", True, self.BLACK)
        self.screen.blit(start_text, (self.WIDTH // 2 - start_text.get_width() // 2, self.HEIGHT // 2))

        quit_text = self.SMALL_FONT.render("Press ESC to Quit", True, self.BLACK)
        self.screen.blit(quit_text, (self.WIDTH // 2 - quit_text.get_width() // 2, self.HEIGHT // 1.5))

        pygame.display.update()

    def handle_menu_input(self, event):
        '''
        handles the input for menu
        args: 
        event (var) event determines when there is an input through a keyboard
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.in_menu = False
                self.game = Guessing(self.word_list)
                self.used_letters = Used_Letters()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    def draw_game(self):
        '''
        draws each part of the game on the screen, starting with the hangman, then the correct and incorrect words, then the lives. it also updates the inputs as results
        args:
        hangman_img_path (str) - a string that is the pathway to the stage the hangman is at
        hangman_img (Surface) - the image from the assets folder that matches with the stage of the hangman displayed in the game
        word_text (Surface) - the word being guessed, unguessed letters will display as "_" while guessed letters are shown as the letter itself displayed in the game
        correct_text (Surface) - the correct letters being guessed displayed in the game
        incorrect_text (Surface) - the incorrect letters being guessed displayed in the game
        lives_left (int) - the number of lives left
        live_text (Surface) - the number of lives left that is displayed in the game
        result_message (str) - whether you have won or lost
        result_text (Surface) - the result message displayed in the game
        '''
        self.screen.fill(self.WHITE)
        
        hangman_img_path = self.game.hangman.get_hangman_stage()
        hangman_img = pygame.image.load(hangman_img_path).convert()
        hangman_img = pygame.transform.scale(hangman_img, (200, 200))
        self.screen.blit(hangman_img, (50, 50))
        
        word_text = self.FONT.render(self.game.display_word(), True, self.BLACK)
        self.screen.blit(word_text, (300, 175))
        
        correct_text = self.SMALL_FONT.render(self.used_letters.display_correct(), True, self.BLACK)
        self.screen.blit(correct_text, (20, self.HEIGHT - 120))
        
        incorrect_text = self.SMALL_FONT.render(self.used_letters.display_incorrect(), True, self.RED)
        self.screen.blit(incorrect_text, (20, self.HEIGHT - 70))
        
        lives_left = len(self.game.hangman.hangman_stages) - 1 - self.game.hangman.lives
        lives_text = self.SMALL_FONT.render(f"Lives Left: {lives_left}", True, self.BLACK)
        self.screen.blit(lives_text, (self.WIDTH - 200, 20))
        
        result_message = self.update()
        if result_message:
            result_text = self.FONT.render(result_message, True, self.RED)
            self.screen.blit(result_text, (self.WIDTH // 2 - result_text.get_width() // 2, self.HEIGHT - 50))
        
        pygame.display.update()
    
    def handle_game_input(self, event):
        '''
        handles the input for guesses
        args: 
        event (variable) event determines when there is an input through a keyboard
        '''
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()
            if letter.isalpha() and len(letter) == 1:
                if letter not in self.used_letters.correct_letters and letter not in self.used_letters.incorrect_letters:
                    if letter in self.game.word:
                        self.used_letters.add_correct(letter)
                    else:
                        self.used_letters.add_incorrect(letter)
                    self.game.guess(letter)
        
    def update(self):
        '''
        updates game state
        return:
        returns the result of the game
        '''
        return self.game.get_result_message()