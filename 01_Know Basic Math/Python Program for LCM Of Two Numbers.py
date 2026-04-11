def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM is:", lcm(num1, num2))