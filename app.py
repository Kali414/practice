print("Hello world")
n=int(input("Enter the number"))

def prime(n):
    cnt=0
    for x in range(1,n**0.5+1):
        if(n%x==0):
            cnt+=1

        if(n%(n/x)==0):
            cnt+=1

    
    if(cnt>2):
        print(f"{n} is not a prime number")

    else:
        print(f"{n} is a prime number")