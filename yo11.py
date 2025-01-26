def prime(lower,upper):
    num=lower
    count=0
    while(num<=upper):
        c=0
        for i in range(1,num+1):
            if (num%i==0):
                c+=1
        if (c==2):
            print(num,"This a prime number")
            count+=1
        num+=1
    print(count, "->This the number of prime numbers")
lower=int(input("Lower: "))
upper=int(input("Upper: "))
prime(lower,upper)