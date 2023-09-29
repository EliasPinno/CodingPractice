def validIPAddresses(string):
    solution = []
    for i in range(1,min(4,len(string)-2)): # Where we place our first .
        for j in range(i+1,min(i+4,len(string)-1)): # where we place our second dot
            for k in range(j+1,min(j+4,len(string))): # Where we place our third dot
                val1 = string[0:i]
                val2 = string[i:j]
                val3 = string[j:k]
                val4 = string[k:]
                vals = [val1,val2,val3,val4]
                isValid = True
                print(vals)
                for val in vals:
                    isValid = isValid and validateStringForIP(val)
                if isValid:
                    solution.append(".".join(vals))
        # Write your code here.
    return solution

def validateStringForIP(string):
    return string == str(int(string)) and int(string) <= 255

# O(1) time and space