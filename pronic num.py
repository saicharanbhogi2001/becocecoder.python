def pronic(n):
    for i in range(1,n//2+1):
        if i*(i+1)==n:
            return True
    return False


n=int(input())
print(pronic(n))
