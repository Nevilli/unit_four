def draw_card():
    pass


def main():
    value1 = draw_card()
    value2 = draw_card()
    value3 = draw_card()
    print("you drew a", value1)
    print("you also drew a", value2)
    total = value1 + value2
    print("your total is", total)
    hit_or_stay = input("would you like to hit or stay?")
    if input("hit") 