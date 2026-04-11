def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

def lcm_of_three(a,b,c):
    return lcm(lcm(a,b), c)
    
print(lcm_of_three(4, 6, 8))