def sum_of_digits(n):
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit

    return result

res = sum_of_digits(651)
print(f"sum of digits of 651 is {res}")