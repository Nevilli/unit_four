import random


def draw_card():
    return random.randint(1, 10)


def main():
    value1 = draw_card()
    value2 = draw_card()
    value3 = draw_card()
    draw_card()
    print("you drew a", value1)
    draw_card()
    print("you also drew a", value2)
    total = value1 + value2
    print("your total is", total)
    hit_or_stay = input("would you like to hit or stay?")
    if hit_or_stay == "hit":
        draw_card()
        print("you drew a", value3)
        total2 = total + value3
        print("your new total is", total2)
        if total2 > 21:
            print("you have lost")
    else:
        value4 = draw_card()
        value5 = draw_card()
        draw_card()
        print("the dealer drew a", value4)
        draw_card()
        print("the dealer dre a", value5)
        total3 = value4 + value5
        print("the dealer's total is", total3)


main()
