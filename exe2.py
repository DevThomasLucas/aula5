x = [1, 2, 3, 3, 2, 1]
def pali1(x):
    n = len(x)
    y = []
    for i in range (n-1, -1 -1):
        y.append (x[i])
        return y == x 

'''''''''
def pali2(x):
    n = len (x)
    for i in range (0,n // 2):
        if x[i]! = x[n-i-1]:
            return false
        return true
'''''''''