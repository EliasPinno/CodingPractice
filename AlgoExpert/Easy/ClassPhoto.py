def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    print(redShirtHeights)
    print(blueShirtHeights)
    if redShirtHeights[0] > blueShirtHeights[0]:
        return verifyRow1FitsBehindRow2(redShirtHeights, blueShirtHeights)
    return verifyRow1FitsBehindRow2(blueShirtHeights, redShirtHeights)

def verifyRow1FitsBehindRow2(row1, row2):
    for i in range(len(row1)):
        if row2[i] >= row1[i]:
            return False
    return True

#O(nlogn) time, O(1) space