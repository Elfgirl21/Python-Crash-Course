responses ={}

polling_flag = True

while polling_flag:
    name = input("What is your name? ")
    response = input("What is your dream vacation? ")

    responses[name] = response

    repeat = input("Would another person like to anser? (yes/no)")
    if repeat == 'no':
        polling_flag = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response}.")