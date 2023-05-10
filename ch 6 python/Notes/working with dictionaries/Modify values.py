"""alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")"""

alien_0 = {'x_position': 0, 'y_postion': 25, 'speed': 'medium'}
print(f"Orginal position: {alien_0['x_position']}")

#move alien to right
#determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #must be a fast alien.
    x_increment = 3

#new position is the old plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")