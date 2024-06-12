def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    return quotient

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    quotient = divide(dividend, divisor)
    print(f"The quotient is {quotient}")

if __name__ == "__main__":
    main()
