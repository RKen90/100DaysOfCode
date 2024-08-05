# if/else statement

'''
if condition:
    do this
else:
    do this
'''

water_level = 50
if water_level > 80:
    print("drain water")
else: 
    print("continue")
    
    
'''
Is user over 120cm?
'''

height = input("Welcome to the Rollercoaster! Please input your height in cm:\n")
#convert str to int
height = int(height)

# Logic block - are you greater than 120cm
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Please do some growing!")