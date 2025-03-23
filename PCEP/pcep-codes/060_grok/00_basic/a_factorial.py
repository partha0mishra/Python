# factorial.py
def factorial(n):
    if n < 0:
        #return "Factorial not defined for negative numbers"
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")