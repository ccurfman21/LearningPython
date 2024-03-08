"""
Author: Cory Curfman
Date:03/07/2024

Purpose: Testing/Learning Python - Hangman

"""

import pygame
from pygame.locals import *
import os
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
ALPH = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.SysFont("Arial", 30)

def drawRect(screen, color, rect):
    pygame.draw.rect(screen,color,rect)
    
def drawCirc(screen, color, circ):
    pygame.draw.circle(screen,color,circ)
    
def drawText(text, font, color, x, y):
    img = font.render(text,True,color)
    screen.blit(img, (x, y))
    
def read_file(file):
     #read files
    if os.path.exists(file):
        with open(file, "r") as fo:
            list = [line.strip() for line in fo.readlines()]
        return list

    
def main():
    vertBeam = pygame.Rect((200,100,10,400))
    horizBeam = pygame.Rect((vertBeam.left,vertBeam.top,200,10))
    noose = pygame.Rect((horizBeam.right,horizBeam.top,10,50))
    base = pygame.Rect((vertBeam.left/2,vertBeam.bottom,200,10))
    gallow = [vertBeam,horizBeam,noose,base]
    
    
    leftArm = pygame.Rect((100,500,200,10))
    rightArm = pygame.Rect((100,500,200,10))
    body = pygame.Rect((100,500,200,10))
    leftLeg = pygame.Rect((100,500,200,10))
    rightLeg = pygame.Rect((100,500,200,10))
    
    lettersRemainingList = ALPH
    lettersCorrect = []
    lettersIncorrect = []

    # Start game
    choices = read_file('fruit.txt')
    num_of_choices = len(choices)
    computerChoiceIndex = random.randint(0,num_of_choices-1) #get random index to choose
    compChoice = choices[computerChoiceIndex] #get computers choiced based off index
    lettersList = [*compChoice]
    print(lettersList)
    
    run = True
    while run:
        
        offset = 20
        for letter in ALPH:
            if letter in lettersRemainingList:
                font_color = WHITE
            elif letter in lettersCorrect:
                font_color = GREEN
            elif letter in lettersIncorrect:
                font_color = RED
            drawText(letter,font,font_color,offset,10)
            offset += 30
            
        for seg in gallow:
            drawRect(screen,WHITE,seg)
              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                key = str(pygame.key.name(event.key))
                if key in lettersList:
                    if key not in lettersCorrect:
                        lettersCorrect.append(key)
                else:
                    lettersIncorrect.append(key)
                
        
               
        pygame.display.update() 
        pygame.display.flip()

       
        
        
        
        
        
        
        
        
        
        
        
        
             
    pygame.quit()
    
    
    # making file callable
if __name__ == "__main__":
    main()
