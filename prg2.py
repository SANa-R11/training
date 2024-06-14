N = int(input("N = "))
arr = []

print("Enter the array:")
for i in range(0,N):
    k = int(input())
    arr.append(k)

print("Array:", arr)

X=int(input("X = "))
print("Index value:")
for i in range (0,N):
    if X==arr[i]:
        print(i)

   