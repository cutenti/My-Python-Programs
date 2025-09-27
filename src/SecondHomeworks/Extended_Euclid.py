def extended_gcd(a, b):
    remainder0, remainder1 = a, b
    factorA0, factorA1 = 1, 0
    factorB0, factorB1 = 0, 1

    while remainder1 != 0:
        quotient = remainder0 // remainder1
        remainder0, remainder1 = remainder1, remainder0 - quotient * remainder1
        factorA0, factorA1 = factorA1, factorA0 - quotient * factorA1
        factorB0, factorB1 = factorB1, factorB0 - quotient * factorB1

    return remainder0, factorA0, factorB0
A, B = int(input()), int(input())
gcd, factorA, factorB = extended_gcd(A, B)
print(f"GCD = {gcd}")
print(f"({factorA}) * {A} + ({factorB}) * {B} = {gcd}")