from art import logo
import random
import os

def clear():
    os.system('clear')

def face_to_num(cards, current_score):
    """Converts face cards to numerical values."""
    for i in range(len(cards)):
        if cards[i] == "Jack" or cards[i] == "Queen" or cards[i] == "King":
            cards[i] = 10
        elif cards[i] == "Ace":
            # Decide whether to treat Ace as 1 or 11 based on the current hand
            if current_score + 11 <= 21:
                cards[i] = 11
            else:
                cards[i] = 1
    

def play_blackjack():
    """Starts Game"""
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    
    player_cards = [random.choice(cards), random.choice(cards)]
    face_to_num(player_cards, sum(player_cards))
    player_score = sum(player_cards)

    computer_cards = [random.choice(cards), random.choice(cards)]
    face_to_num(computer_cards, sum(computer_cards))
    computer_score = sum(computer_cards)

    print(logo)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while True:
        new_card = input("Type \"y\" to get a new card, type \"n\" to pass: ").lower()
        if new_card == "y":
            player_cards.append(random.randrange(0,len(cards)))
            face_to_num(player_cards, sum(player_cards))
            player_score = sum(player_cards)
            break
        elif new_card == "n":
            break  
        else:
            print("Please input a valid answer.")


while True:
    play = input("Do you want to play a game of Blackjack? y/n: ").lower()

    if play == "y":
        play_blackjack()
        break
    elif play == "n":
        clear()
        break  
    else:
        print("Please input a valid answer.")
