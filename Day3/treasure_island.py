print("Welcome to Treasue Island! Your mission is to find the treasure.")

direction = input("You're at a cross roads. Where do you want to go? Type 'left' or 'right\n")
if direction.lower() == 'left':
    swim = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if swim.lower() == 'wait':
        door = input("You arrive at the island unharmed. There is a hosue with 3 doors. One Red, one yellow and one blue. Which colour do you choose?\n")
        if door.lower() == "red":
            print("You are burned by fire. Game over")
        elif door.lower() == "blue":
            print("You were eaten by beasts. Game over")
        elif door.lower() == "yellow":
            print("You win!")
        else:
            print("Game over")
    else:
        print("You were attacked by trout. Game Over")

else:
    print("You fall into a hole. Game Over")    