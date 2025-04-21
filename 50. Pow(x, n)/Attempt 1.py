
def myPow(x: float, n: int):
    

    if n == 0:
        return 1
    
    if n < 0:
        return 1 / myPow(x, -n)
    
    if n % 2 == 0:
        return myPow(x * x, n // 2)
    
    return x * myPow(x, n - 1)

print(myPow(2.0, 10))
