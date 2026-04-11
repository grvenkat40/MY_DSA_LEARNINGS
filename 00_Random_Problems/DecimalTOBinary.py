decimal = 10
bin = ""
while decimal > 0:
    num = decimal%2
    bin += str(num)
    decimal //= 2

print(bin)