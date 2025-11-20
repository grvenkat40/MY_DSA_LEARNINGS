def set_rightmost_unset_bit(n):
    return n | (n+1)

def main():
    n = 10  # binary: 1010
    result = set_rightmost_unset_bit(n)
    print("Number after setting rightmost unset bit:", result)  # Output: 11

if __name__ == "__main__":
    main()