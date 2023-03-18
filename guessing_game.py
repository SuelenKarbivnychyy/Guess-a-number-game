""" This a guessing game where the player has to guess a number from 1 to 100 """
import random
import art


def return_number_of_attempts(difficult):
    """define the attempt number."""

    if difficult == "easy":
        attempts = 10      
        return attempts            
    else:
        attempts = 5        
        return attempts
    

def check_guess(guess, choose_number):
    """Check if the guess is correct"""

    if guess < 1 or guess > 100:
        print("Not value number, Please choose a number beetween 1 and 100.")
        return False
    elif int(guess) == choose_number:
        print("You won")       
        return True
    else:
        if guess > choose_number:
            print("Your guess is too high.")                
            return False
        elif guess < choose_number:
            print("Your guess is too low.")                 
            return False   


def play_game(choose_number):
    """Play the guessing number game"""
    print(art.logo)

    print("Welcome to the guessing number game.\nI'm thinking of a number between 1 and 100.")
    difficult = input("Choose your difficult typing 'easy' or 'hard': ").lower()
    number_of_attempts = return_number_of_attempts(difficult) 

    guess = int(input(f"You have {number_of_attempts} attempts remaining, make a guess: "))
    number_of_attempts -= 1
    is_game_over = False

    while is_game_over == False and check_guess(guess, choose_number) == False: 

        if number_of_attempts > 0:
            guess = int(input(f"You have {number_of_attempts} attempts remaining, make a guess: "))
            number_of_attempts -= 1            
            print(guess)
        else:
            print("You are out of attempts. You lose") 
            is_game_over = True        

choose_number1 = random.randint(1, 101)      
play_game(choose_number1)          

  