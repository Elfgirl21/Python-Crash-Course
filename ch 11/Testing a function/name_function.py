def get_formatted_name(first, last, middle=''): #original didn't have middle
    """Generate a neatly formatted full nume"""
    if middle: #optional
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

#works for both 'Janis Joplin' & 'Wlofgang Amadeus Mozart'