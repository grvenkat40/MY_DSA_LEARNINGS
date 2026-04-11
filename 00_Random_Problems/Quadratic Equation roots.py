import math

def find_roots(a, b, c):
    D = b*b-4*a*c
    
    if D > 0:
        root1 = (-b + math.sqrt(D))/(2*a)
        root2 = (-b - math.sqrt(D))/(2*a)
        print(root1, root2)
    elif D == 0:
        root = -b/(2*a)
        print(root)
    else:
        real = -b/(2*a)
        img = math.sqrt(-D)/(2*a)
        print(real, img)


find_roots(a = 1, b = -3, c = 2)