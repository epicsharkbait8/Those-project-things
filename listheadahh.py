groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    print(groceries)
    getrid = input("what do you want to get rid of?")
    if getrid in groceries:
        groceries.remove(getrid)
    elif getrid == "stop":
        break
print("Your new list is" + str(groceries))