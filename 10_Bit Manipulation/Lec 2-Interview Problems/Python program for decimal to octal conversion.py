def decimal_to_octal(n):
    if n == 0:
        return '0'
    octal = ""
    while n > 0:
        rem = n % 8
        octal = str(rem) + octal
        n = n//8
    return octal
print(decimal_to_octal(83))