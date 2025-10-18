def t(n):
    if n==1:
        return 1
    else:
        return t(n-1)+(n-1)




while True:
    try:
        n = int(input("Enter a number"))
        if n == -1:
            break
        if n<1:
            print("Enter a  num grater than 0.")
            continue

    except ValueError:
        print("Enter a valid number.")
        continue

    x = t(n)
    print(f"result:" , x)
    
print("Program terminated.")
    
