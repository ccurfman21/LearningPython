"""
Author: Cory Curfman
Date:03/07/2024

Purpose: Testing/Learning Python - Rock Paper Scissors

"""

# imports
import random


# Global Variables


# Classes


# Functions


def askUser(choices): #function to ask user to choose
    
    while True:
        userChoice = input(f"Pick {'/'.join(choices)}: ").lower() #getting user input
        if userChoice in choices: #check if input is valid
            break
        print(f'Invalid choice.')
            
    return userChoice


def printGameResults(status,compChoice,userChoice):
    print(f"I picked {compChoice} and you picked {userChoice}. You {status}!") #give user results

def main():
    choices = ['rock', 'paper', 'scissors'] #list of choices
    
    while True:   
        computerChoiceIndex = random.randint(0,len(choices)-1) #get random index to choose
        compChoice = choices[computerChoiceIndex] #get computers choiced based off index
        userChoice = askUser(choices) #go get users choice

        #check for tie
        if userChoice == compChoice: 
            print("Tie! Go again.")
        else:
            break
        
    #find winner/loser
    if compChoice == 'rock' and userChoice == 'scissors' or \
        compChoice == 'paper' and userChoice == 'rock' or \
        compChoice == 'scissors' and userChoice == 'paper':
            
        result = 'Lose'
        printGameResults(result,compChoice,userChoice) 
        
    elif userChoice == 'rock' and compChoice == 'scissors' or \
        userChoice == 'paper' and compChoice == 'rock' or \
        userChoice == 'scissors' and compChoice == 'paper':
            
        result = 'Win'
        printGameResults(result,compChoice,userChoice) 
       
    else:
        print('No winners')
        
    
        
# making file callable
if __name__ == "__main__":
    main()
