#while loop
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#infinite loop!
while True:
    print("\nPlease tell your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}")