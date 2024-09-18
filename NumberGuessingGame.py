from random import randint

# Constants for the number of turns allowed in easy and hard modes
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """
    Compares the user's guess with the actual answer.
    
    Args:
        user_guess (int): The user's guessed number.
        actual_answer (int): The correct number to guess.
        turns (int): The number of remaining turns.
    
    Returns:
        int: Updated number of remaining turns if the guess is incorrect.
        bool: True if the guess is correct.
    """
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1  # Decrease turns by 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1  # Decrease turns by 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True  # Return True when the correct guess is made

# Function to set difficulty level
def set_difficulty():
    """
    Prompts the user to choose a difficulty level.
    
    Returns:
        int: Number of turns based on the chosen difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS  # Return 10 turns for easy difficulty
    else:
        return HARD_LEVEL_TURNS  # Return 5 turns for hard difficulty

# Main game function
def game():
    """
    Starts the number guessing game where the player has to guess a randomly chosen
    number between 1 and 100 within a limited number of turns based on the difficulty level.
    """
    # Choosing a random number between 1 and 100
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate the random number to be guessed
    answer = randint(1, 100)
 
    # Set the number of turns based on the chosen difficulty level
    turns = set_difficulty()
    
    guess = 0  # Initialize the guess variable
    
    # Loop until the user guesses the correct answer or runs out of turns
    while guess != answer:
        print(f"You have {turns} turns remaining to guess the number.")
        
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        
        # Check the user's guess and update the number of turns
        turns = check_answer(guess, answer, turns)
        
        # If turns run out, end the game
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  # Exit the game if no turns are left
        
        # If the guess was incorrect but there are remaining turns, prompt to guess again
        elif guess != answer:
            print("Guess again.")
        else:
            print("You win!")  # This line is redundant, but left for clarity

# Start the game when the script is executed
game()
