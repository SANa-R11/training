N = int(input("N = "))
arr = []

print("Enter the array:")
for i in range(N):
    k = int(input())
    arr.append(k)

print("Array:", arr)  
element_count = {}

for element in arr:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1


print("Duplicate elements:")
for element, count in element_count.items():
    if count > 1:
        print(f"{element}: {count} times")
