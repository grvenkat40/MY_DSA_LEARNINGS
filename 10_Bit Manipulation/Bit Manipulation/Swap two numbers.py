def swap_two_numbers(a, b):
    a = a ^ b   # 1100
    b = a ^ b   # 0100
    a = a ^ b   # 1000
    return a, b

a = 4  # 0100
b = 8  # 1000
print(swap_two_numbers(a,b))