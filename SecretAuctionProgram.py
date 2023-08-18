import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\                         
'''

print(logo)
print("Welcome to the secret auction program.")
bidders = dict()
bid_list = list()


def clear():
    os.system('cls')


def highest_bidder(bid_dict):
    for keys in bid_dict:
        bid_list.append(bid_dict[keys])
    bid_list.sort(reverse=True)
    winner = int(bid_list[0])
    for names in bid_dict:
        bid_amount = int(bid_dict.get(names))
        if bid_amount == winner:
            winner_name = names
    print(f"The winner is {winner_name} with a bid of ${winner}")


def auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bidder = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")
    if other_bidder == 'yes':
        clear()
        auction()
    else:
        highest_bidder(bidders)
    return


def main():
    auction()
    exit()


main()
