"""
Pseudocode:

    1) create a int variables called preferredCity, starting city, and gasTank intialized to 0
    2) create an outer loop 
    x) adjusts the city_distances array with append and remove so that we keep the city_distances array circular in the problem
    x) create a inner loop 
    x) iterate through the city_distances array
    x) if at the starting city, then add fuel at i multiplied by the mpg to the gasTank, then continue the loop
    x) else subtract city_distances at i from the gasTank
    x) inner loop is done 
    x) if mpg >= 0 then preferredCity = startingCity, and break, we found the preferred city
    x) if not outer loop continues
    
"""

from collections import deque

def hamiltonSolution(city_distances, fuel, mpg):
    """
    Given an array of city distances, array of fuel per city, and a positive int mpg,
    return the index of the preferred starting city where the mpg >= 0 when traversing the
    entire city_distances array
    """

    # code


"""
Test Case:
"""

city_distances = [5, 25, 15, 10, 15] 
fuel = [1, 2, 1, 0, 3] 
mpg = 10

# the output should be 4
print(hamiltonSolution(city_distances, fuel, mpg))