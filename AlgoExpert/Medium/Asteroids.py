from collections import deque

def collidingAsteroids(asteroids):
    solution = deque()
    if len(asteroids) < 2:
        return asteroids
    solution.append(asteroids[0])
    for i in range(1,len(asteroids)):
        print(list(solution))
        topOfStack = solution.pop()
        currentAsteroid = asteroids[i]
        # We don't need to manage a collision
        if topOfStack < 0 or (topOfStack > 0 and currentAsteroid > 0):
            solution.append(topOfStack)
            solution.append(currentAsteroid)
        else: # We are attempting to add a negative to the stack with a positive top
            # New asteroid is destroyed
            if topOfStack ==  abs(currentAsteroid):
                continue # Both are destroyed: add neither to stack
            if topOfStack > abs(currentAsteroid):
                solution.append(topOfStack)
            else: # We need to start clearing the stack
                while topOfStack > 0 and topOfStack < abs(currentAsteroid) and len(solution) > 0:
                    topOfStack = solution.pop()
                if topOfStack ==  abs(currentAsteroid):
                    continue # Both are destroyed: add neither to stack
                elif topOfStack < 0: # We destroyed all positive astroids
                    solution.append(topOfStack)
                    solution.append(currentAsteroid)
                elif topOfStack > abs(currentAsteroid):
                    solution.append(topOfStack)
                elif len(solution) == 0: # we destroyed all asteroids
                    solution.append(currentAsteroid)
                else: # we found a positive that beat the incoming
                    solution.append(topOfStack)            
    return list(solution)
# O(n) time, O(n) space.