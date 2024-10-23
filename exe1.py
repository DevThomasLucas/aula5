"Apresentar os dois maiores valores de um vetor."
x = [1, 2, 3, 3, 2, 1]


n = len(x)
ma1, ma2 = x[0], x[1]
if ma2 > ma1:
        ma1, ma2 = ma2, ma1
        for i in range(2,n):
            if x[i]>ma2:
                ma2 = x[i]
            if ma2 > ma1:
                ma1, ma2 = ma2, ma1
print (ma1, ma2)

"limitante superior O(n)"
