def insertion_sort_asc(arr):
    
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
                   

# ---------- MAIN PROGRAM ---------

n = int(input("Enter how many numbers: "))
arr = []
total = 0

for i in range(n):
    while True:
        try:
            num = int(input("Enter number: "))
            arr.append(num)
            total = total + num
            break
                   
        except ValueError:
            print("Invalid input!.. plz enter an integer:")

print("Original Array:", arr)
insertion_sort_asc(arr)
print("Sorted Array (Asscending):", arr)

#----Count----------------
m = int(input("Enter count number: "))
count = arr.count(m)

if count > 0:
    print(count)

#-------Remove-------------

q = int(input("Enter a number to remove: "))

if q in arr:
    while q in arr:
        arr.remove(q)
    
else:
    print(f"The number is not found in the array.")

print("Updated Array:", arr)


print("min", arr[0])
print("min", arr[-1])
avg = total / n
print("Total =", total)
print("Average =", avg)



