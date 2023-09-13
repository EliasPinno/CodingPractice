def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    totalSpeed = 0
    for i in range(0, len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    
    return totalSpeed
# O(nlogn) speed, O(1) space