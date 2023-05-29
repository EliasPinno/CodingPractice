class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        digitList = []
        xLoop = x
        while xLoop > 0:
            digitList.append(xLoop % 10)
            xLoop = xLoop // 10
        print(digitList)
        # List should be in descending order
        for i in range(0, len(digitList)//2):
            leftDigit = digitList[i]
            rightDigit = digitList[len(digitList)-i-1]
            if leftDigit != rightDigit: 
                return False
        return True
            
# O(k) where k is number of digits? More digits = more loop steps, etc.