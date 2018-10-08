# Liam Neville
# 10/5/18
# This is a program that lets the user play a game of blackjack against the dealer
import random


def draw_card():
    """
    This function draws a random card
    :return: Random integer that represents card value
    """
# Aces are always one
    return random.randint(1, 10)


def dealer_cards():
    """
    This function draws two cards for the dealer and adds them together
    :return: Dealer's total
    """
    value4 = draw_card()
    value5 = draw_card()
    draw_card()
    print("The dealer drew a", value4)
    draw_card()
    print("The dealer also drew a", value5)
    total3 = value4 + value5
    print("The dealer's total is", total3)
    return total3


def win(player, dealer):
    """
    This function determines who wins the round
    :param player: player total
    :param dealer: dealer total
    :return: None
    """
    if player > dealer:
        print("You have won!")
    elif player < dealer:
        print("The dealer has won")
    else:
        print("It's a tie!!!")


def main():
    value1 = draw_card()
    value2 = draw_card()
    value3 = draw_card()
    draw_card()
    print("You drew a", value1)
    draw_card()
    print("You also drew a", value2)
    total = value1 + value2
    print("Your total is", total)
    hit_or_stay = input("Would you like to hit or stay?")
    if hit_or_stay == "hit":
        draw_card()
        print("You drew a", value3)
        total = total + value3
        print("Your new total is", total)
        if total > 21:
            print("You have lost")
        else:
            total3 = dealer_cards()
            win(total, total3)
    elif hit_or_stay == "stay":
        total3 = dealer_cards()
        win(total, total3)


main()
