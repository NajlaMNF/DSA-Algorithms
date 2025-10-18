def f(n):
    if n<= 1:
        return 1
    else:
        return f(n-1)+ f(n-2)



while True:
    try:
        n = int(input("Enter a no neagtive number:"))
        if  n== -1:
            break

        if n <0:
            print("enter a valid number.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue

    x = f(n)
    print(f"Result: ", x)
print("Program terminated.")
