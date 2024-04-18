n = int(input("Enter how many elements in Array: "))
Array = []

for i in range(n):
    print("Enter element", i, ":",end="")
    Array.append(int(input()))

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if Array[j] < Array[min_index]:
            min_index = j
    Array[i], Array[min_index] = Array[min_index], Array[i]

print("Sorted Array:",end="")
for element in Array:
    print(element, end=" ")
