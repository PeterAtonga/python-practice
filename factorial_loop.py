# function to complete factorial using a loop

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
