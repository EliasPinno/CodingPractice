def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
    solution = [intervals[0]]
    for i in range(1, len(intervals)):
        startOfInterval = intervals[i][0]
        endOfInterval = intervals[i][1]
        if startOfInterval <= solution[len(solution)-1][1]:
            solution[len(solution)-1][1] = max(solution[len(solution)-1][1], endOfInterval)
        else:
            solution.append(intervals[i])
        
    return solution

# O(nlogn) time, O(1) space