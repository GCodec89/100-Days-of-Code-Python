import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_winner(player_score, computer_score):
    if player_score > computer_score:
        print("You win 😃")
    elif player_score < computer_score and computer_score > 21:
        print("You win 😃")
    elif player_score < computer_score:
        print("You lose 😤")
    else:
        print("It's a draw 🙃")

def check_ace(hand):
    if sum(hand) > 21:
        for i, n in enumerate(hand):
            if n == 11:
                hand[i] = 1

def player_hand(hand):
    hand.append(random.choice(cards))
    check_ace(hand)
    if len(hand) < 2:
        hand.append(random.choice(cards))
    player_score = sum(hand)
    return player_score

def computer_hand(hand):
    hand.append(random.choice(cards))
    check_ace(hand)
    computer_score = sum(hand)
    return computer_score

def blackjack(player_cards, computer_cards, blackjack_is_on):
    while blackjack_is_on:
        player_score = player_hand(player_cards)

        computer_score = computer_hand(computer_cards)

        print(f"\t\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\t\tComputer's first card: {computer_score}")

        continue_game = True
        while continue_game:
            continue_game_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_game_input == "y":
                player_score = player_hand(player_cards)
                print(f"\t\tYour cards: {player_cards}, current score: {player_score}")
                print(f"\t\tComputer's first card: {computer_score}")
                if player_score > 21:
                    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
                    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
                    continue_game = False
            else:
                while computer_score < 17:
                    computer_score = computer_hand(computer_cards)
                print(f"\tYour final hand: {player_cards}, final score: {player_score}")
                print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
                check_winner(player_score, computer_score)
                continue_game = False

        if player_score > 21:
            print("You went over. You lose 😭")

        blackjack_is_on = False

game_is_on = True
while game_is_on:
    player_res = 0
    computer_res = 0
    p_cards = []
    c_cards = []
    play = input("Do you want to play a game of 🃏Blackjack🃏? Type 'y' or 'n': ").lower()
    if play == "y":
        print(f"\n" * 30)
        print(logo)
        blackjack_on = True
        blackjack(p_cards, c_cards, blackjack_on)
    else:
        print("Goodbye 😎")
        game_is_on = False
