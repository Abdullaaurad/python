n = int(input("Enter how many elements in Array: "))
arr = []

for i in range(n):
    print("Enter element", i, ":",end="")
    arr.append(int(input()))

n = len(arr)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array:",end="")
for element in arr:
    print(element, end=" ")
