import random

# Greet the player
print("Welcome to the game of Blackjack")

def deal_card():
    """Returns a random card from the deck.
    Cards include numbers 2-10, with the face cards (J, Q, K) represented by 10, 
    and Ace (11), which can be worth either 11 or 1.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Deck of cards
    card = random.choice(cards)  # Randomly pick a card from the deck
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards.
    - A score of 0 represents a Blackjack (21 with 2 cards).
    - If there's an Ace (11) and the score exceeds 21, it is counted as 1.
    """
    # Check if there's a Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Return 0 to represent Blackjack
    
    # Adjust for Ace if the score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Remove the Ace counted as 11
        cards.append(1)  # Add the Ace counted as 1
    
    return sum(cards)  # Return the sum of cards as the score

def compare(u_score, c_score):
    """Compares the user's score and the computer's score to determine the winner."""
    if u_score == c_score:
        return "Draw 😊"
    elif c_score == 0:
        return "Loose, Opponent has BlackJack 😮"
    elif u_score == 0:
        return "Win with a BlackJack 😎"
    elif u_score > 21:
        return "You went over. You lose 😪"
    elif c_score > 21:
        return "Opponent went over. You win 😁😁"
    elif u_score > c_score:
        return "You win 😊😎"
    else:
        return "You lose 😡😡"

def play_game():
    """Plays a full game of Blackjack, handling the player's and computer's moves."""
    user_cards = []  # Stores player's cards
    computer_cards = []  # Stores computer's cards
    is_game_over = False  # Flag to track when the game ends

    # Deal two cards for both the user and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)  # Calculate the user's score
        computer_score = calculate_score(computer_cards)  # Calculate the computer's score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")  # Show only one of the computer's cards

        # Check if the game is over (either Blackjack or score > 21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Deal another card to the user
            else:
                is_game_over = True  # End the player's turn

    # Computer's turn: Computer must draw cards until its score is 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show the final hands and scores for both player and computer
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Compare the scores to declare the winner

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ? ") == 'y':
    print("\n" * 20)  # Clear the screen for the new game
    play_game()  # Start a new game of Blackjack
