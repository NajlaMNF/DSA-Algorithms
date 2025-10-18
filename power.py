def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


while True:
    try:
        base = float(input("Enter the base number (-1 to exit): "))

        if base == -1:
            print("Program terminated.")
            break

        exp = int(input("Enter the exponent (non-negative integer): "))

        if exp < 0:
            print("Please enter a non-negative exponent.")
            continue

        print(f"{base} raised to the power {exp} is:", power(base, exp))

    except ValueError:
        print("Invalid input. Please enter numeric values.")
