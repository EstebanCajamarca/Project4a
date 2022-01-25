# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/24/2022

# The following formula can be used to determine the distance an object falls due to gravity in a specific time period:
# d = (1/2)gt2
# where d is the distance in meters, g is 9.8, and t is the time in seconds that the object has been falling. Write a
# function named fall_distance that takes the time in seconds as an argument. The function should return the distance
# in meters that the object has fallen in that time. For example if the function is passed the value 3.2,
# then it should return the value 50.176. Your function does not need to print anything out - just return a value.

def fall_distance(time):
    """Returns the fallen distance of an object in meters with the given time in seconds.
    g=9.8 is the force of gravity."""
    return (9.8 * time * time) / 2

# Tests
# dist = fall_distance(4.5)
# print(dist)
# print(fall_distance(3.2))
