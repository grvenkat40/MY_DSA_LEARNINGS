def hexa_to_decimal(hex):
    l = len(hex)
    decimal = 0
    pos = 0
    for i in range(l-1, -1 ,- 1):
        if '0' <= hex[i] <= '9':
            digit = int(hex[i])
            decimal += digit * pow(16, pos)
            pos += 1
        elif 'A' <= hex[i] <= 'F':
            digit = ord(hex[i]) - 55
            decimal += digit * pow(16, pos)
            pos += 1
    return decimal

print(hexa_to_decimal("1A"))