N = int(input("N="))
arr = []
print("Enter the array:")
for i in range(N):
    k = int(input())
    arr.append(k)

print(arr) 

sorted_arr = sorted(arr)
print(sorted_arr)

for i in range(N,0):
    print(arr[i])