"""
Author: Cory Curfman
Date:03/07/2024

Purpose: Testing/Learning Python - Hangman

"""

import pygame
from pygame.locals import *
import os
import random
import copy
import time

#initialize pygame
pygame.init()

# set constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
ALPH = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#create main surface
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#set font
font = pygame.font.SysFont("Arial", 30)

#create the head class
class head:    
    def __init__(self, radius, x, y):
        self.radius = radius
        self.center = (x, y)

# Drawing Rectatngles Function
def drawRect(screen, color, rect):
    pygame.draw.rect(screen,color,rect)

# Drawing Lines Function
def drawLine(screen,color,start_pos,end_pos,width):
    pygame.draw.line(screen,color,start_pos,end_pos,width)

# Drawing Circles Function
def drawCirc(screen, color, center, radius):
    pygame.draw.circle(screen,color,center,radius)

# Displaying Text
def drawText(text, font, color, x, y):
    img = font.render(text,True,color) #make text an image
    screen.blit(img, (x, y)) #display image
    pygame.display.flip() #update display for the image
    
# Read txt file
def read_file(file):
    if os.path.exists(file):
        with open(file, "r") as fo:
            list = [line.strip() for line in fo.readlines()] #remove the /n from each element of the list
        return list

# Display the result of the game
def endGame(result,text):
    img_width = 500
    img_height = 300
    ans = 'The answer is: ' + text
    img = pygame.image.load("you_" + result + ".png").convert() #load and convert image for pygame
    img = pygame.transform.scale(img,(img_width,img_height)) #change size of image
    x = (SCREEN_WIDTH - img_width)/2
    y = (SCREEN_HEIGHT - img_height)/2
    screen.blit(img,(x,y)) #display image
    drawText(ans,font,GREEN,x + 100,y + 200) #put answer on screen
    pygame.display.flip() #update display
    time.sleep(3) #delay for 3 seconds
    
    

    
def main():
    #set up the gallow
    vertBeam = pygame.Rect((200,100,10,400)) 
    horizBeam = pygame.Rect((vertBeam.left,vertBeam.top,200,10))
    noose = pygame.Rect((horizBeam.right,horizBeam.top,10,50))
    base = pygame.Rect((vertBeam.left/2,vertBeam.bottom,200,10))
    gallow = [vertBeam,horizBeam,noose,base]
    
    #make copy so we do not change ALPH
    lettersRemainingList = ALPH.copy()
    
    #get word
    choices = read_file('food.txt')
    num_of_choices = len(choices)
    computerChoiceIndex = random.randint(0,num_of_choices-1) #get random index to choose
    compChoice = choices[computerChoiceIndex] #get computers choiced based off index
    lettersList = [*compChoice] #make string a list of letters
    
    #setup underlines list
    userUnderlines = ' __ ' * len(compChoice)
    
    #initalize
    lettersCorrect = []
    lettersIncorrect = []
    line_width = 5
    
    #draw underlines for answer
    drawText(userUnderlines,font,WHITE,380,525) 
    
    #draw the gallow       
    for seg in gallow:
        drawRect(screen, WHITE, seg)

    #start game loop
    run = True
    while run:
        
        #print letters onto screen with updates for guessed letters
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

        
        #event handler
        for event in pygame.event.get():
            
            #stop loop if game window is closed
            if event.type == pygame.QUIT:
                run = False
            
            #get key pressed
            elif event.type == KEYDOWN:
                key = str(pygame.key.name(event.key))
                
                #check if key is in the answer
                if key in lettersList:
                    occurance = [k for k in lettersList if k == key] #find how many times the letter is in the answer       
                    if key not in lettersCorrect:
                        for j in range(len(occurance)):
                            lettersCorrect.append(key) #add letters to the correct list to track
                            
                #make sure a letter is pressed 
                elif key in ALPH:
                    if key not in lettersIncorrect:
                           
                           lettersIncorrect.append(key) #add letters to incorrect list to track
                    
                if key in lettersRemainingList:
                    lettersRemainingList.remove(key) #remove letters that can be guessed

                #display answer letters guessed
                offset = 390
                for letter in lettersList:
                    if letter == key or letter in lettersCorrect:
                        font_color = WHITE
                    elif letter not in lettersCorrect:
                        font_color = BLACK
                    drawText(letter,font,font_color,offset,525) 
                    pygame.display.update() 
                    offset += 43
                    
        #draw head
        if len(lettersIncorrect) == 1:
            radius = 30
            x = noose.centerx
            y = noose.bottom + radius
            head_center = head(radius,x,y).center
            head_radius = head(radius,x,y).radius
            drawCirc(screen, RED, head_center, head_radius)
        
        #draw body 
        elif len(lettersIncorrect) == 2:
            bodyLen = 150
            y = head_center[1] + head_radius
            body_start_pos = (x, y)
            body_end_pos = (x, y + bodyLen)
            drawLine(screen, RED, body_start_pos,body_end_pos,line_width)
        
        #draw arm 1
        elif len(lettersIncorrect) == 3:
            armLen = 50
            y = body_end_pos[1] - int(bodyLen/2)
            arm_start_pos = (x, y)
            arm_end_pos = (x + armLen, y - armLen)
            drawLine(screen, RED, arm_start_pos,arm_end_pos,line_width)
        
        #draw arm 2
        elif len(lettersIncorrect) == 4:
        
            y = body_end_pos[1] - int(bodyLen/2)
            arm_start_pos = (x, y)
            arm_end_pos = (x - armLen, y - armLen)
            drawLine(screen, RED, arm_start_pos,arm_end_pos,line_width)
        
        #draw leg 1
        elif len(lettersIncorrect) == 5:
            legLen = 50
            y = body_end_pos[1]
            leg_start_pos = (x, y)
            leg_end_pos = (x + legLen, y + legLen)
            drawLine(screen, RED, leg_start_pos,leg_end_pos,line_width)
        
        #draw leg 2 
        elif len(lettersIncorrect) == 6:
            
            y = body_end_pos[1]
            leg_start_pos = (x, y)
            leg_end_pos = (x - legLen, y + legLen)
            drawLine(screen, RED, leg_start_pos,leg_end_pos,line_width)
            
        #update the display
        pygame.display.update() 
        
        #check if game is over and end it
        if len(lettersList) == len(lettersCorrect):
            status = 'win'
            endGame(status,compChoice)
            run = False
            
        elif len(lettersIncorrect) == 6:
            status = 'lose'
            endGame(status,compChoice)
            run = False
        
    pygame.quit()
    
    
    # making file callable
if __name__ == "__main__":
    main()
