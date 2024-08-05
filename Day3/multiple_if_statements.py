print("Welcome to the Rollercoaster!")

height = input("What is your height in CM?\n")
height = int(height)
price = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = input("What is your age?\n")
    age = int(age)
    if age >= 18:
        price = 12
        print(f"Please pay ${price}")
    else:
        price = 7
        print(f"Please pay ${price}")
    photo = input("Would you like a photo? Answer Y or N\n")
    if photo == "Y" or photo == "y":
            price += 3
            
    print(f"Your final bill is ${price}")    
else:
    print("You are too short! Shorty short pants.")