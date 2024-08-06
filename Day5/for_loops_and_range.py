# Using a loop without a list

# Range Function
for number in range(1, 11):
    print(number)
    
    
# With a atep size of 3
for number in range(1, 11, 3):
    print(number)
    

# Adding up all of the numbers from 1-100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)