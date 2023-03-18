""" This a guessing game where the player has to guess a number from 1 to 100 """

#pseudocode:
#welcome the user and explain the game
#Tell the user to choose a difficult easy or hard
#Dependind on what difficult he choose tell him how many attempts he has
#Tell him to make a guess
#if guess is correct, the game ends and the user won
#if guess is not correct:
#   check if he still have attempts
#   if does, display how many attempts remainding and ask to guess again
#   if user out of attempts he lose

import random


def return_number_of_attempts(difficult):
    """define the attempt number."""

    if difficult == "easy":
        attempts = 10      
        return attempts
    elif difficult == "hard":
        attempts = 5        
        return attempts
    else:
        return "This is not value"

def play_game(guess):
    # attempts = return_number_of_attempts(difficult)

    if guess < 1 or guess > 100:
        print("Not value number, Please choose a number beetween 1 and 100.")
        # return is_game_over
    elif int(guess) == choose_number:
        print("You won")
        is_game_over = True
        return is_game_over
    else:   
         
        if attempts != 1:
            attempts -= 1 
            print(f"THIS SHOULD BE THE NUMBER OF ATTEMPTS: {attempts}")
            if guess > choose_number:
                print("Your guess is too higly.")                
                return is_game_over
            elif guess < choose_number:
                print("Your guess is too low.")                 
                return is_game_over           
        else:
            print("You are out of attempts")
            is_game_over = True 
            return is_game_over  
        


print("Welcome to the guessing number game.\nI'm thinking of a number between 1 and 100.")
difficult = input("Choose your difficult typing 'easy' or 'hard': ").lower()
choose_number = random.randint(1, 101)
# print(choose_number)

attempts = return_number_of_attempts(difficult)

is_game_over = False
while not is_game_over:  
    
    guess = int(input(f"You have attempts remaining, make a guess: "))
    # print(guess)

play_game(guess)        