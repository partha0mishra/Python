# factorial.py
def factorial(n):
    if n < 0:
        return None
    elif n > 100:
        raise ValueError("Number too large! Max allowed is 100.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter a number (or 'quit' to exit): ")
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            num = int(user_input)
            print(f"The factorial of {num} is {factorial(num)}")
        except ValueError as e:
            print(f"Error: {e}")  # Catches both invalid input and our custom exception
            # print ("Please enter a valid number of 'quit' ")