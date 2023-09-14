def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True
# O(n) time, O(1) space