my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #copy list

"""This doesn't work
friend_foods = my_foods not copying, just associating
prints the same list twice
"""
my_foods.append('cannoli')
friend_foods.append('ice cream') #ensure they're separate lists

print("My favourite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)