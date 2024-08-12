gavel = '''
    _______
 __|_______|_____
 \             /
  \___________/
       ||
       ||
       ||
       ||
       ||
       
'''

print(gavel)
print("Welcome to the Silent Auction")
name_and_bid = {}
bidding_war = True
while bidding_war == True:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n£")
    name_and_bid[name] = bid
    
    valid_input = False
    while not valid_input:
        continue_bid = input("Are there any other bidders? Y or N?\n").upper()
        if continue_bid == 'N':
            bidding_war = False
            valid_input = True
        elif continue_bid == 'Y':
            valid_input = True
            print('\n' * 100)  # Clears the screen
            print(gavel)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    
    
highest_bidder = max(name_and_bid, key = name_and_bid.get)
highest_bid = name_and_bid[highest_bidder]
print(f'The Highest bid is £{highest_bid} by {highest_bidder}')


