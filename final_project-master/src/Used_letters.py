class Used_Letters:
    def __init__(self):
        '''
        Initializes an object with two lists for used letters, one for correct and another for incorrect
        args:
        correct_letters (list) - starts as an empty set and will become a list of correct letters
        incorrect_letters (list) - starts as an empty set and will become a list of incorrect letters
        '''
        self.correct_letters = set()
        self.incorrect_letters = set()
    
    def add_correct(self, letter):
        '''
        adds correct letters to the set of correct letters
        args: 
        letter (str) - letter to add to the correct set
        '''
        self.correct_letters.add(letter)
    
    def add_incorrect(self, letter):
        '''
        adds incorrect letters to the set of incorrect letters
        args:
        letter (str) - letter to add to the incorrect set
        '''
        self.incorrect_letters.add(letter)
    
    def display_correct(self):
        '''
        returns a string with all correct letters
        '''
        return "Correct: " + " ".join(sorted(self.correct_letters))
    
    def display_incorrect(self):
        '''
        returns a string with all incorrect letters
        '''
        return "Incorrect: " + " ".join(sorted(self.incorrect_letters))