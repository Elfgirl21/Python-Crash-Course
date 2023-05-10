from random import choice


def get_winning_ticket(lottery):

    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(lottery)
        if pulled_item is not winning_ticket:
            winning_ticket.append(pulled_item)
    
    return winning_ticket

def check_ticket(play_ticket, winning_ticket):
    for element in play_ticket:
        if element not in winning_ticket:
            return False

    return True 

def random_ticket(lottery):
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(lottery)
        if pulled_item is not ticket:
            ticket.append(pulled_item)
    return ticket

lottery = ['1', 'l', '5', '3', 'f', 'r', '9', '4', 'h', 'a']
winning_ticket = get_winning_ticket(lottery)

plays = 0
won = False

max_plays = 100

while not won:
    new_ticket = random_ticket(lottery)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_plays:
        break

    if won:
        print("We have a winning ticket!")
        print(f"My ticket {new_ticket}")
        print(f"The winning ticket {winning_ticket}")
        print(f"It took {plays}!")
    else:
        print(f"I tired {plays} and I still didn't win.")
        print(f"My ticket {new_ticket}")
        print(f"The winning ticket {winning_ticket}")

