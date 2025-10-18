def insertion_sort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        
        while i>-1 and arr[i]>key:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1] = key


n = int(input("Enter student amount:"))
arr=[]
for i in range(n):
    while True:
        try:
            
            num = int(input("Enter marks: "))
            arr.append(num)
            break

        except ValueError:
            print("enter valid number.")
   

    
print("original array: ",arr)
            
insertion_sort(arr)
print("sorted array: " , arr)


if n % 2 !=0:
    median = arr[n//2]
else:
    median = (arr[n//2-1]-arr[n//2])/2
                  
print("median: " , median)
print("Range: ",arr[-1]- arr[0])                                

           
            

