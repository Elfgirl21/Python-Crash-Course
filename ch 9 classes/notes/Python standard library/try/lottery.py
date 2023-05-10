from random import choice

lottery = [1, 'l', 5, 3, 'f', 'r', 9, 4, 'h', 'a']

winning_ticket = []

print("Any ticket with the following wins a prize:")

while len(winning_ticket) < 4:
    pulled_item = choice(lottery)
    if pulled_item is not winning_ticket:
        winning_ticket.append(pulled_item)
    
for x in winning_ticket:
    print(x)
