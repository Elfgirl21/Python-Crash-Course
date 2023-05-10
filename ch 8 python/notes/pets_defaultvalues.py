#default values
def describe_pet(pet_name, animal_type = 'dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'willie')

#order had to be changed. Default makes it unnecessary to specify
#type of animal as arg
#python interprets this a positional arg

describe_pet(pet_name= 'harry', animal_type= 'hamster') #python ignores default