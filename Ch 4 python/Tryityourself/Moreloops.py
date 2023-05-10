my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #copy list

my_foods.append('cannoli')
friend_foods.append('ice cream') #ensure they're separate lists

print("My favourite foods are:")
for x in my_foods:
    print(x)

print("\nMy friends favorite foods are:")
for y in friend_foods:
    print(y)