# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(art.winner)

bids = {}
bidding = True

while bidding:
    name = input("Enter Your Name:\n")
    amount = int(input("Enter your bidding amount: $"))
    bids[name] = amount
    add_members = input("Are there any other bidders? Yes or NoYou Want add members to bid type 'YES' or else type 'NO'.\n").lower()

    if add_members == "no":
        bidding = False
        find_highest_bidder(bids)
    elif add_members == "yes":
        print("\n" * 100)


