def sumcube(n):
    if n == 1:
        return 1
    else:
        return sumcube(n - 1) + n * n * n

while True:
    try:
        num = int(input("Enter a positive integer (-1 to exit): "))

        if num == -1:
            print("Program terminated.")
            break
        elif num <= 0:
            print("Please enter a positive number.")
            continue

        print("Sum of cubes of first", num, "numbers is:", sumcube(num))

    except ValueError:
        print("Invalid input. Please enter an integer.")
