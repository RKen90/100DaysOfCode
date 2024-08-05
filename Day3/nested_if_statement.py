print("Welcome to the Rollercoaster!")

height = input("What is your height in CM?\n")
height = int(height)

if height >= 120:
    print("You can ride the rollercoaster")
    age = input("What is your age?\n")
    age = int(age)
    if age >= 18:
        print("Please pay $12")
    else:
        print("Please pay $7")
    
else:
    print("You are too short! Shorty short pants.")