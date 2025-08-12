from art import logo

print(logo)
print("Welcome to the secret auction program!")

auction_is_on = True
auction_dictionary = {}
right_bid = False
while auction_is_on:
    name = input("What is your name? ")

    # handles bid
    while not right_bid:
        bid_str = input("What's your bid? ")
        bid_str = bid_str.replace(",", ".") # handles bid with "," instead of "."
        try:
            bid = float(bid_str)
            if "." in bid_str:
                decimal_part = bid_str.split(".")[1]
                if len(decimal_part) > 2: # handles decimal places
                    print("Please enter a number with at most 2 decimal places.")
                    continue
            right_bid = True
        except ValueError: # handles bid with symbols or letters
            print("Please enter a valid number.")
    right_bid = False

    auction_dictionary[name] = bid

    more_biders = input("Are there any other biders? Type 'yes' or 'no'.\n")
    if more_biders == "yes":
        auction_is_on = True
    else:
        auction_is_on = False

    print("\n" * 30)

max_bid = 0
for name in auction_dictionary:
    if auction_dictionary[name] > max_bid:
        max_bid = auction_dictionary[name]
        winner = name

print(f"The winner is {name} with a bid of ${max_bid}")
