# Trivial n^2 solution

def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    n = len(distances)
    for startingCity in range(len(distances)):
        print("Starting city is at: {}".format(startingCity))
        gas = 0
        loop = 0
        currentCity = startingCity
        while loop < n:
            print("Loop city is at: {}".format(currentCity))
            gas += fuel[currentCity]*mpg
            distance = distances[currentCity]
            if gas < distance:
                print("Break at {}".format(currentCity))
                break
            gas -= distance
            currentCity = (currentCity + 1) % n
            loop += 1
        if currentCity == startingCity and loop != 0:
            return currentCity
    return -1
# O(n^2) time, O(1) space