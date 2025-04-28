# function to find the sum of digits of a number

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total
