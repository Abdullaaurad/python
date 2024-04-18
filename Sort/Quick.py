def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

n = int(input("Enter how many elements in Array: "))
Array = []
for i in range(n):
    print("Enter element", i, ":",end="")
    Array.append(int(input()))

quick_sort(Array)
print("Sorted Array:",end="")
for element in Array:
    print(element, end=" ")
