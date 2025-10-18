def insertion_sort_asc(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key

    #main

n = int(input("Enter how many numbers: "))
arr = []
total = 0

for i in range (n):
    while True:
        try:
            num = int(input("Enter number : "))
            arr.append(num)
            total = total + num
            break

        except ValueError:
            print("Enter valid number")
            print()
            continue

print("Original array: ", arr)
insertion_sort_asc(arr)
print("Sorted array (Ascending): ", arr)


#count
m = int(input("Enter count number: "))
count = arr.count(m)
if count>0:
    print(count)


#remove
q = int(input("Enter number to remove: "))
if q in arr:
    while q in arr:
        arr.remove(q)

else:
    print(f"The number is not found in this array")

print("The updated array: ", arr)


#min, max, 
print("Minimum: ", arr[0])
print("Maximum: ", arr[-1])

#range
arr_range = arr[-1] - arr[0]
print("Range: ", arr_range)


#tot
print("total: ", total)

#avg/mean
avg = total/n
print("Average: ", avg)

#median
if n % 2!= 0:
    median = arr[n//2]
else:
    median = (arr[n//2 - 1] + arr[n//2])/2
print("Median: ", median)

#sep odd and even num
even_num = []
odd_num = []
for x in arr:
    if x % 2 == 0:
        even_num.append(x)
    else:
        odd_num.append(x)
print("Even Numbers: " ,even_num)
print("odd Numbers: " ,odd_num)


#reverse the array
arr.reverse()
print("Reversed array: " , arr)


