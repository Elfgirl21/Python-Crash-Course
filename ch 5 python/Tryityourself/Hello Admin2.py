usernames =[]

if usernames == []:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
    print("We need to find some users!")    