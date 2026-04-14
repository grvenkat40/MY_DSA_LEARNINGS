def octalToDecimal(num):
    decimal = 0
    base = 1
    while num > 0:
        last = num % 10
        decimal += (last * base)
        base *= 8
        num = num//10
    return decimal

print(octalToDecimal(512))