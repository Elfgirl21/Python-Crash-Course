alien_0 = {'color': 'green', 'speed': 'slow'}
#use get() to set a default value that will be return if requested jey doesn't exist
#1st arg is key, 2nd arg is optional - pass value to be returned if nothing exist

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#if 'points' exist, get corresponding value, otherwise default
