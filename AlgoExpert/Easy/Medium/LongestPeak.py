def longestPeak(array):
    if len(array) < 3:
        return 0
    # step one: identify peaks and valleys
    # peaks have smaller elements on either side of them
    peaks = []
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peaks.append(i)
    # Step two: radiate out from peaks
    peakLength = 0
    for peak in peaks:
        leftPointer = peak-1
        while leftPointer >= 0 and array[leftPointer] < array[leftPointer+1]:
            leftPointer -= 1
        rightPointer = peak+1
        while rightPointer < len(array) and array[rightPointer] < array[rightPointer-1]:
            rightPointer += 1
        peakLength = max(peakLength, rightPointer-leftPointer-1)
        
    return peakLength
# O(n) time (paths can't be part of multiple peaks)
# space: O(n) technically 1/3 of all elements can be peaks: need to store all these elems