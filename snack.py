"""why snack"""
def main():
    """lol"""
    money = int(input())
    water = int(input())
    snack_number1 = int(input())
    snack_number2 = int(input())
    snack_number3 = int(input())
    left = money - water
    number1 = left % 3
    if number1 == 0:
        number1 = 10
        snack_number1 = snack_number1 * number1
    elif number1 == 1:
        number1 = 15
        snack_number1 = snack_number1 * number1
    elif number1 == 2:
        number1 = 20
        snack_number1 = snack_number1 * number1
    left = left - snack_number1
    number2 = left % 3
    if number2 == 0:
        number2 = 12
        snack_number2 = snack_number2 * number2
    elif number2 == 1:
        number2 = 15
        snack_number2 = snack_number2 * number2
    elif number2 == 2:
        number2 = 18
        snack_number2 = snack_number2 * number2
    left = left - snack_number2
    number3 = left % 3
    if number3 == 0:
        number3 = 5
        snack_number3 = snack_number3 * number3
    elif number3 == 1:
        number3 = 7
        snack_number3 = snack_number3 * number3
    elif number3 == 2:
        number3 = 9
        snack_number3 = snack_number3 * number3
    left = left - snack_number3
    if left < 0:
        print("Now you have %d left.\nYou don't have enough money!"\
            %(money))
    else:
        print("""Now you have %d left.
Here's your order!
Water: %d baht
Snack number 1: %d baht
Snack number 2: %d baht
Snack number 3: %d baht""" %(left, water, \
        snack_number1, snack_number2, snack_number3))
main()
