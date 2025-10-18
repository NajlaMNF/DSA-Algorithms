def Multiply(M,n):
    if n == 1:
        return M
    else:
        return M + Multiply(M, n-1)


while True:
    try:
        M = int(input("Enter 1st num:"))
        if M == -1:
            break
    except ValueError:
            print("Enter valid no")
            continue

    try:
        n = int(input("Enter 2nd num:"))
        if n == -1:
            break
    except ValueError:
            print("Enter valid no")
            continue

    x = Multiply(M,n)
    print(f"result: ", x)
    
print("program terminated")
