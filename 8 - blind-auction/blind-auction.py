import os

def biggest_bidder(bids:dict):
    biggest_bid = max(bids.values())
    for key in bids:
        if bids[key] == biggest_bid: 
            winner = key
            break
    return f"The winner was {winner} with a bid of {biggest_bid} Euros"

dict_bids = {}
finished = False
while not finished:
    client_name = input("What is your name?: ")
    client_bid = int(input("What is your bid in Euros?: "))
    dict_bids[client_name] = client_bid
    another_bid = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if another_bid == "no":
        finished = True
        print(biggest_bidder(dict_bids))
    elif another_bid == "yes":
        os.system("cls")
