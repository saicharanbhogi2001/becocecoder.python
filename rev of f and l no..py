while 1:
    n=int(input())
    c=s=k=0
    t=n
    while n:
        r=n%10
        n=n//10
        c+=1
    c=s=c-1
    n=t
    p=n%10
    q=n//(10**c)
    while n:
        r=n//(10**c)
        n=n%(10**c)
        if c==s:
            r=p
        elif c==0:
            r=q
        k=k*10+r
        c-=1
    print(k)
