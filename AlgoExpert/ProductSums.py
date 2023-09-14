# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return productSumHelper(array,1)

def productSumHelper(array, depth):
    sum = 0
    for item in array:
        if isinstance(item,list):
            sum += productSumHelper(item,depth+1)
        else:
            sum += item
    return sum*depth
# O(n) time where n is the number of elements in all the lists together
# O(d) space where d is the maximum available depth