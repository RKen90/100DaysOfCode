'''
Who will pay the bill?
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
'''

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


print("Welcome to 'Who Will Pay the Bill!?'")
number = random.randint(1, 5)
#print(number)

if number == 1:
    print(friends[0])
elif number == 2:
    print(friends[1])
elif number == 3:
    print(friends[2])
elif number == 4:
    print(friends[3])
else:
    print(friends[4])
    
# Option 2    
print(random.choice(friends))


# Option 3
random_index = random.randint(0, 4)
print(friends[random_index])