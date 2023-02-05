def absolutePermutation(n, k):
    ans = []
    check  = {}
    for i in range(1,n+1):
        cell = check.get(i, i+k)   # Method return the value for the given key if present in the dictionary. If not, then it will return None 
        check[cell] = i
        if cell > n:
            return [-1]
        ans.append(cell)
    return ans

  





