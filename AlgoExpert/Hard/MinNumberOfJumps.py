UNCHECKED = -1

def minNumberOfJumps(array):
    # Write your code here.
    n = len(array)
    memory = [UNCHECKED]*n
    memory[-1] = 0
    return minStepsToEndFromPoint(0,n,array,memory)
    
def minStepsToEndFromPoint(i,n,values,memory):
    # This spot has been explored previously
    if memory[i] != UNCHECKED:
        return memory[i]
    # We are at the end
    if i == n-1:
        return 0
    # We need to calculate the minimum from this spot
    rangeFromSpot = values[i]
    jumpsFromSpot = n # Can't be more jumps then n since we can't go backwards
    for j in range(i+1,i+rangeFromSpot+1):
        if j < n:
            jumpsFromSpot = min(jumpsFromSpot,1+minStepsToEndFromPoint(j,n,values,memory))
    # Write the value into memory so we don't recalculate it ever
    memory[i] = jumpsFromSpot
    return jumpsFromSpot
# O(n) time, O(n) space