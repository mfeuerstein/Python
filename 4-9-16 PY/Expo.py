# Selection sort with ability to specify direction of the sort

def expo(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * expo(base, exp - 1)

def main():
    for exponent in range(5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    
