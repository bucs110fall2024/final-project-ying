import pygame
from src.Controller import Controller 

def main():
    pygame.init()
    controller = Controller()
    controller.main_loop()

if __name__ == '__main__':
    main()
