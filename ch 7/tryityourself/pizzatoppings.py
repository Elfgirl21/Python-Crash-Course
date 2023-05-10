prompt = "\nPlease enter your desired pizza topping."
prompt += "\nWhen you're finished entering pizza toppings, type 'quit'."

while True:
    message = input(prompt)

    if message == 'quit':
        print("\nYour Pizza is finished!")
        break
    else:
        print(f"\n{message.title()} is being added to your pizza.")