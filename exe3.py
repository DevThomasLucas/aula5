def buscabinaria (x,v):
    li, ls = 0 , len(x)-1
    while li >= ls:
        i = (li + ls)//2
        if v == x[i]:
            return i 
        elif v < x [i]:
            ls = i -1
        else:
            li = i - 1 
        return -1 
    
"O(lg n) Algoritmo otimo"