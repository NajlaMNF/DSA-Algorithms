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

for i in range(n):
    while True:
        try:
            num = int(input("Enter number: "))
            arr.append(num)
            break
                   
        except ValueError:
            print("Invalid input!.. plz enter an integer:")

print("Original Array:", arr)
insertion_sort_asc(arr)
print("Sorted Array (Asscending):", arr)


# ---------------- Separate Odd and Even ----------------
even_num = []
odd_num = []
for x in arr:
    if x % 2 == 0:
        even_num.append(x)
    else:
        odd_num.append(x)

print("Even Numbers:", even_num)
print("Odd Numbers:", odd_num)

# ---------------- Reverse the Array ----------------
arr.reverse()
print("Reversed Array:", arr)

