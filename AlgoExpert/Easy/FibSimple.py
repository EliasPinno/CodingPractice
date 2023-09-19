def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)
# O(n) space, O(2^n) time
# Reasoning: O(n) space because while the total space if it was parallelized would be
# 2^n, in reality an entire recursive chain is resolved before another one ever starts.
# Each chain only exists at once and is O(n), so it is O(n) space at any given moment.