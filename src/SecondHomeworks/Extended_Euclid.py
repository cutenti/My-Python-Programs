def extended_gcd(a, b):
    remainder0, remainder1 = a, b
    factor_a0, factor_a1 = 1, 0
    factor_b0, factor_b1 = 0, 1

    while remainder1 != 0:
        quotient = remainder0 // remainder1
        remainder0, remainder1 = remainder1, remainder0 - quotient * remainder1
        factor_a0, factor_a1 = factor_a1, factor_a0 - quotient * factor_a1
        factor_b0, factor_b1 = factor_b1, factor_b0 - quotient * factor_b1

    return remainder0, factor_a0, factor_b0


a, b = int(input()), int(input())
gcd, factor_a, factor_b = extended_gcd(a, b)
print(f"GCD = {gcd}")
print(f"({factor_a}) * {a} + ({factor_b}) * {b} = {gcd}")
