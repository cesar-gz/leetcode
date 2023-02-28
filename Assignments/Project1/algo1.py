"""
Submission for Cesar Gutierrez
"""

def hamiltonSolution(city_distances, fuel, mpg):
    """
    Given an array of city distances, array of fuel per city, and a positive int mpg,
    return the index of the preferred starting city where the mpg >= 0 when traversing the
    entire city_distances array
    """

    gasTank = 0
    size = len(city_distances) - 1

    # Create outer loop that will test each city as a startingCity
    for startingCity in range(size):
      if startingCity == 0:
        # leave city_distances alone
        pass
      else:
        # re-adjust city_distances, so that the startingCity is the first index
        j = 0
        while(j < startingCity):
          # add the first element of city distances array to the back of the array,
          # continue until the new startingCity is the first element of city_distances
          city_distances.append(city_distances.pop(j))
          j += 1
        print(city_distances)

      # iterate through city_distances array
      for k in range(size + 1):
        if k == 0:
          # first city, no need to subtract miles, only here to add fuel
          gasTank += fuel[k] * mpg
          print("fueling up at the first city, our current gas tank can go " + str(fuel[k] * mpg) + " miles \n")
          continue
        else:
          # travel to next city, use gas, subtract
          gasTank -= city_distances[k-1]
          print("at next city, subtracting the distance of " + str(gasTank) + " miles")
          print("our current fuel is " + str(gasTank))
          # at a new city, fuel up
          gasTank += fuel[k] * mpg
          print("fueling up at this city with " + str(fuel[k] * mpg) + " miles")
          print("Our gas tank can go for : " + str(gasTank) + " miles \n")
      if gasTank >= 0:
        return startingCity
      else:
        print("This starting city is not good, our fuel is at " + str(gasTank) + " miles")
        print("----------------------- re running, starting at another city -----------------------\n")
        gasTank = 0
        continue

"""
Test Case:
"""

city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

print("The preferred starting city is at index " + str(hamiltonSolution(city_distances, fuel, mpg)))
