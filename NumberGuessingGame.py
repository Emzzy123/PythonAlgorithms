from random import randint

#Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True
 # function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5


#Choosing a random number between 1 and 100
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)

#Function to set difficulty

#let the user guess a number
guess= int(input("Make a guess: "))