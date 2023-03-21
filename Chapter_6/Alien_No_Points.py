print("\nUsing get() to Access Values\n")
# # Returns a KeyError
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# Will return key if it exists (try using color instead of points in call)
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print()

alien_color = alien_0.get('color')
print(alien_color)
print()

# Returns the special value 'None'indicating the absence of of a value
alien_1 = {'color': 'green', 'speed': 'slow'}
point_value = alien_1.get('points')
print(point_value)
print()