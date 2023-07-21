class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisonDuration = 0
        poisonOffTime = timeSeries[0] + duration
        for i in range(1,len(timeSeries)):
            currentTime = timeSeries[i]
            if currentTime >= poisonOffTime:
                poisonDuration += duration
            else:
                poisonDuration += currentTime - (poisonOffTime - duration)
            poisonOffTime = currentTime + duration
        poisonDuration += duration
        return poisonDuration
# O(n) time and O(n) space where n is the length of the timeSeries list