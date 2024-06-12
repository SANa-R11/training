def main():
    N = int(input("Enter the size N of the array: "))
    
    if N > 20:
        print("Array size should not exceed 20.")
        return

    Arr = []
    print("Enter the array elements:")
    for i in range(N):
        element = int(input())
        Arr.append(element)

    Arr.sort(reverse=True)

    if N > 1:
        print("The greatest element is:", Arr[0])
        print("The second greatest element is:", Arr[1])
    else:
        print("The greatest element is:", Arr[0])
        print("There is no second greatest element as the array has only one element.")

if __name__ == "__main__":
    main()
