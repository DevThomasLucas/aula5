"Apresentar os dois maiores valores de um vetor."
x = [14,12,53,45,55,49,86,88,97,3,5]
def exercico1 (x):
    n = len(x)
    ma1, ma2 = x[0], x[1]
    if ma2 > ma1:
        ma1, ma2 = ma2, ma1
    for i in range(2,n):
        if x[i]>ma2:
            ma2 = x[i]
            if ma2 > ma1:
                ma1, ma2 = ma2, ma1
    return ma1, ma2

"limitante superior O(n)"