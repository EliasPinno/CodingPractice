def taskAssignment(k, tasks):
    # Write your code here.
    indexedTasks = list(enumerate(tasks))
    indexedTasks.sort(key=lambda x: x[1])
    solution = []
    for i in range(len(indexedTasks)//2):
        solution.append( [indexedTasks[i][0], indexedTasks[len(indexedTasks)-i-1][0]] )
    return solution
# O(nlogn) time, O(n) space