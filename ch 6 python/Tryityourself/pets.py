pet_1 = {'name': 'emily', 'kind': 'dog', 'owner': 'sarah' }
pet_2 = {'name': 'roadie', 'kind': 'cat', 'owner': 'ben' }
pet_3 ={'name': 'skyer', 'kind': 'rat', 'owner': 'asha' }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pet's name: {pet['name'].title()}")
    print(F"Pet kind: {pet['kind'].title()}")
    print(f"Pet owner: {pet['owner'].title()}\n")