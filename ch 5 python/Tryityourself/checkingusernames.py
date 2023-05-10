#have to copy 1st list for case insensitive.
current_users = ['elfgirl21', 'Dreamup34', 'Bumbum@90', '20Jackieboy', '2Marki89']

new_users = ['elfgirl21', 'Bumbum@90', '89Bowieboy', 'Beau@357', 'Uni@90man']

for current_user in current_users:
    if current_user in new_users:
        print(f"{current_user.title()} is taken. Enter a different username.")
    else:
        print("Username is available.")