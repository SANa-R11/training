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

    X = int(input("Enter the number X: "))

    count = 0
    for element in Arr:
        if element == X:
            count += 1

    print(f"The occurrence of X is {count} times")

if __name__ == "__main__":
    main()
