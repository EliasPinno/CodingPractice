def minimumWaitingTime(queries):
    queries.sort()
    totalWaitTime = 0
    for i in range(0, len(queries)-1):
        totalWaitTime += queries[i]*(len(queries)-1-i)
    return totalWaitTime
# O(log(n)) time, O(1) space