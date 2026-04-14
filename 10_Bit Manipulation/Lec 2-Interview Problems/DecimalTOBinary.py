decimal = 12
bin = ""
while decimal > 0:
    num = decimal%2
    bin = str(num) + bin
    decimal //= 2

print(bin)