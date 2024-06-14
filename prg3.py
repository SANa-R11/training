N = int(input("N = "))
arr = []
sum=0
count=0
print("Enter the array:")
for i in range(0,N):
    k = int(input())
    arr.append(k)

print("Array:", arr)

for k in range(2,N):
    sum=arr[0]+arr[1]+arr[k]
    
    if sum==0:
        count+=1
        print(count)

    
              
