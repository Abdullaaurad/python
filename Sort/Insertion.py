n = int(input("Enter how many elements in Array: "))
arr = []

for i in range(n):
    print("Enter element", i, ":",end="")
    arr.append(int(input()))

n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted Array:",end="")
for element in arr:
    print(element, end=" ")
