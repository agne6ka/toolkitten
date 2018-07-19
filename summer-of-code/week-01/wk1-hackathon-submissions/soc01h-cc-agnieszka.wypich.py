'''
Task: Calculate the size of a continent you are standing on in your 11 x 11 world in Civilization III.

Bonuses for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world
'''

#imports
from random import choice
from pprint import pprint

# random world generator
def worldGenerator(size = 11):
    world = [[choice([0,1]) for item in range(size)] for item in range(size)]
    pprint(world)

worldGenerator(20)
worldGenerator()
