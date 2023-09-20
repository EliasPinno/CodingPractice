def threeNumberSort(array, order):
    orderMap = {order[0]: 1, order[1]: 2, order[2]:3}
    array.sort(key=lambda x: orderMap[x])
    return array

# O(n) time, O(1) space. Maybe a bit too literal?