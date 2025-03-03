import random
random_num = random.randint(0, 100)

count = 0

while True:
    guess = int(input("guess a number \n"))
    count += 1
    if guess < random_num:
        print("the number you want is higher")
    elif guess > random_num:
        print("the nuber you want is lower")
    else:
        print("YATTA, it took you " + str(count) + " tries.")
        break
