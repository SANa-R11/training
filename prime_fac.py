import math

N=int(input("N= "))
def primeFac(N):
    maxprime=-1
    while N%2==0:
        maxprime=2
        N>>=1
    for i in range(3,int(math.sqrt(N)) + 1,2):
        while N%i==0:
            maxprime=i
            N=N/i
    if N>2:
        maxprime=N
    return int(maxprime)

print(primeFac(N))
