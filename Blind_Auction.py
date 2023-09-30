import os
from art import logo

auction_book={}
play_again=True
print(logo)
print("Welcome to the secret auction program.")

while play_again==True:
    name=input("Please enter your name: ")
    bid=int(input("Please enter your bid: ₹"))
    auction_book[name]=bid
    again=input("Are there any other bidders? Types 'yes' or 'no'.\n").lower()
    os.system('cls')
    print(logo)
    if again=="no":
        play_again=False

def highest_bidder(auction_book):
    highest=0
    for key in auction_book:
        if auction_book[key]>highest:
            highest=auction_book[key]
            winner_name=key
    return highest,winner_name

highest, winner_name = highest_bidder(auction_book)
print(f"The winner is {winner_name} with a bid of ₹{highest}")
    
