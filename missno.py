def find_missing_number(arr):
    N = len(arr) + 1
    expected_sum = N * (N + 1) // 2
    
    actual_sum = sum(arr)
    
    missing_number = expected_sum - actual_sum
    return missing_number

def main():
    N = int(input("Enter the size N of the array : "))
    
    print("Enter the array elements:")
    Arr = []
    for _ in range(N):
        element = int(input())
        Arr.append(element)

    missing_number = find_missing_number(Arr)
    print(f"The missing number is {missing_number}")

if __name__ == "__main__":
    main()
