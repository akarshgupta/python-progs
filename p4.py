    n = int(input())
    s=0
    b=0
    while(n!=0):
        if(n>=10 and n<100):
            a=n*int(math.pow(10,(b+1)))   
            b=b+1                    
            s=s+a
            n=n-1
            if ((n-1)%10>=1):
                continue
        else:
            a=n*int(math.pow(10,b))
        b=b+1                    
        s=s+a
        n=n-1
    print (s)
