def getNthFib(n, memory = {1:0, 2:1}):
    if n in memory:
        return memory[n]
    memory[n] = getNthFib(n-1, memory) + getNthFib(n-2, memory)
    return memory[n]
# O(n) time, O(n) space
# No more then O(n) entries in the memory, which each need to only be computed once
# No more then O(n) recursions at any time, so O(n) space