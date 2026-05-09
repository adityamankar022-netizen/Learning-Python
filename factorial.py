# Python function to calculate factorial

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


# Example usage
num = 5
print(f"Factorial of {num} is {factorial(num)}")