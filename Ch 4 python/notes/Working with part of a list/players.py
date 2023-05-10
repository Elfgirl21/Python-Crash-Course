#index 0-4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #1st item through 3rd [0,1,2]
print(players[1:4]) #2nd item through 4th [1,2,3]
print(players[:4]) #1st through 4th [0,1,2,3]
print(players[2:]) #3rd item through end [2,3,5]
print(players[-3:]) #last 3 players
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())