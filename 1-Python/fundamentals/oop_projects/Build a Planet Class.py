
# Build a Planet Class
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should create a class named Planet.
# The Planet class should have an __init__ method that:
# Has four parameters: self, name, planet_type, and star.
# Raises a TypeError with the message name, planet type, and star must be strings if any of the arguments passed in is not a string type.
# Raises a ValueError with the message name, planet_type, and star must be non-empty strings if any of the arguments passed in is an empty string.
# Assigns the values passed in to the instance attributes name, planet_type, and star.
# The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
# The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
# You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
# You should print each planet object to see the __str__ method output.
# You should call the orbit method on each planet object and print the result.



class Planet:
    def __int__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        