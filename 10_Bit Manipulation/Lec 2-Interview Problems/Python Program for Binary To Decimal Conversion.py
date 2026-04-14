def binary_to_Decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit)*(2 ** power)
        power += 1
    return decimal
print(binary_to_Decimal("1011"))