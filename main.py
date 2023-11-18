from art import logo
import random
import os

player_win = 0
computer_win = 0
number_of_games = 0

def clear():
    os.system('clear')

def face_to_num(cards):
    """Converts face cards to numerical values and handles Ace values."""
    updated_cards = []

    for card in cards:
        if card in ["Jack", "Queen", "King"]:
            updated_cards.append(10)
        elif card == "Ace":
            # Use 11 as the default value for Ace
            updated_cards.append(11)
        else:
            updated_cards.append(card)

    # Check if there are Aces in the hand and adjust their value to 1 if needed
    while sum(updated_cards) > 21 and 11 in updated_cards:
        updated_cards[updated_cards.index(11)] = 1

    return updated_cards


def determine_winner(player_score, computer_score):
    global player_win
    global computer_win
    if player_score > 21:
        computer_win += 1
        print("You bust, you lose.")
    elif computer_score > 21:
        player_win += 1
        print("Computer busts, you win.")
    elif player_score == 21:
        player_win += 1
        print("You have a BLACKJACK! You win.")
    elif computer_score == 21:
        print("Computer has a BLACKJACK! You lose.")
        computer_win += 1
    elif player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        computer_win += 1
        print("You lose.")
    else:
        print("It's a tie.")

def play_blackjack(first_play=True):
    """Starts Game"""
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    
    player_cards = [random.choice(cards), random.choice(cards)]
    player_cards_new = face_to_num(player_cards)
    player_score = sum(player_cards_new)

    computer_cards = [random.choice(cards), random.choice(cards)]
    computer_cards_new = face_to_num(computer_cards)
    computer_score = sum(computer_cards_new)

    global player_win
    global computer_win
    global number_of_games

    if first_play:
        print(logo)  # Display logo only during the first play

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while True:
        new_card = input("Type 'y' to get a new card, type 'n' to pass: ").lower()
        if new_card == "y":
            player_cards.append(random.choice(cards))
            player_cards_new = face_to_num(player_cards)
            player_score = sum(player_cards_new)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                break
        elif new_card == "n":
            break
        else:
            print("Please input a valid answer.")

    while computer_score < 17:
        new_card = random.choice(cards)
        print(f"Computer drew: {new_card}")
        computer_cards.append(new_card)
        computer_cards_new = face_to_num(computer_cards)
        computer_score = sum(computer_cards_new)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    determine_winner(player_score, computer_score)
    number_of_games += 1
    print(f'''You have played {number_of_games} times.
Computer won {computer_win} times.
You won {player_win} times.'''
    )

# Use flag to determine if it's the first play
first_play_flag = True

while True:
    play_again = input(f"Do you want to {'play a game of Blackjack' if first_play_flag else 'play again'}? y/n: ").lower()
    if play_again != "y":
        clear()
        break
    else:
        play_blackjack(first_play=first_play_flag)  # Pass first_play flag
        first_play_flag = False  # Set the flag to False for subsequent plays