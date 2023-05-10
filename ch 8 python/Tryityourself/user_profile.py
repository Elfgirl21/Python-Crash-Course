def build_profile(first, last, **user_info):
    #build a dic containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('lauren', 'harms', hair = 'blonde', eye = 'blue', height = 164)
print(user_profile)