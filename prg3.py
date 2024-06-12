def Missing():

    N=int(input("N= "))
    arr=[]
    print("enter the array:")
    for i in range(N):
        arr=int(input(""))

        arr.sort()
        prev=0
        for i in arr:
            if i==prev+1:
                prev=i
            else:
                return prev+1
    
print(Missing())