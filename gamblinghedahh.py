import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces



def spin_wheel(spaces):
    return random.choice(spaces)


def play_game():
    money = 1000
    spaces = generate_wheel()

    while True:
        print("you have $" + str(money) + " to gamble.")
        bet = input("How much you betting? ")
        bet = int(bet)

        if bet >= money:
            print("You aint even got that much")
            break
        color = input("What color do you bet on?")
        print("The wheel is spinning, Good luck!")
        time.sleep(3)
        landed = spin_wheel(spaces)
        print("It landed on " + landed + ".")

        if landed == color:
            money = money + bet
            print("Yatta! you now got $" + str(money))
        else:
            money = money - bet
            print("HAHAHAHA IMAGINE LOSING, now get lost, you now got $" + str(money))       


        if money <= 0:
            break

        play_again = input("wanna play again?")
        if play_again == "no":
            break
            
play_game()

print("F outta here!")