# Using get() Method to Access Values
alien_0 = {"color": "green", "speed": "slow"}
print(alien_0["points"])    # intentional KeyError

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)