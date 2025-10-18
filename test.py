

# Step 1: Input 9 daily sales values
sales = []
for i in range(9):
    value = int(input(f"Enter sales for day {i+1}: "))
    sales.append(value)

# Step 2: Sort the list using Insertion Sort
for i in range(1, len(sales)):
    key = sales[i]
    j = i - 1
    while j >= 0 and sales[j] > key:
        sales[j + 1] = sales[j]
        j -= 1
    sales[j + 1] = key

# Step 3: Compute the Median (middle value)
n = len(sales)
if n % 2 == 1:
    median = sales[n // 2]
else:
    median = (sales[n//2 - 1] + sales[n//2]) / 2

# Step 4: Compute the Mode manually
mode = sales[0]
max_count = 0

for num in sales:
    count = sales.count(num)
    if count > max_count:
        max_count = count
        mode = num

# Step 5: Display the results
print("\nSorted sales:", sales)
print("Median:", median)
print("Mode:", mode)
