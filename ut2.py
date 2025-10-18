def f(num):
    if num==1:
        return 1
    else:
        return (f(num-1))+ num
    





while True:
    try:
        num = int(input("Enter num:"))
        if num == -1:
            break
        else:
            result = f(num)
            print("Result: " ,num)

        if num<0 :
            print("Enter a value greater rthan 0.")
            continue
        
    except ValueError:
        print("Enter valid number")

    
print("Program terminated")
