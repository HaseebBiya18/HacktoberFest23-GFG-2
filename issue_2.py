num = int(input("Enter a number: "))
if num < 2:
    print("Prime factors are not defined for numbers less than 2.")
else:
    factors = []
    divisor = 2

    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1

    print(f"Prime factors of {num} are: {factors}")
