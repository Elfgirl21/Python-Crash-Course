person_1 = {'first_name':'asha', 'last_name': 'moonstrike', 'age': 22, 'city': 'euless'}
person_2 = {'first_name':'eren', 'last_name': 'yeager', 'age': 19, 'city': 'paladies'}
person_3 = {'first_name':'levi', 'last_name': 'marks', 'age': 30, 'city': 'arlington'}

people = [ person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = f"\t {person['age']}"
    city = f"\t {person['city']}"
    print(f"{full_name.title()}")
    print(age)
    print(city.title())