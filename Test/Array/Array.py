Array = []

def Create(x):
    for i in range(x):
        print("Enter element", i, ":", end="")
        y = int(input())
        Array.append(y)

def search(value, x):
    found = 0
    for i in range(x):
        if Array[i] == value:
            print("The value is found at index =", i)
            found = 1

    if found == 0:
        print("Value is not in Array")

def remove(value):
    found = 0
    for i in Array:
        if i == value:
            Array.remove(i)
            found = 1

    if found == 0:
        print("Value is not in Array")

x = int(input("Enter how many elements to enter:"))
Create(x)
print("Array =", Array)

z = int(input("Which element to search for:"))
search(z, x)

a = int(input("Which element to remove:"))
remove(a)
print("After element removed =",Array)

b = int(input("Enter the element to add:"))
c = int(input("Enter the index at which to add the element:"))
Array.insert(c, b)
print("Array after insertion =", Array)

Array.sort()
print("Array after sorting =",Array)

print("The sum =",sum(Array))
print("The Average =",sum(Array)/len(Array))
array_max = max(Array)
array_min = min(Array)
print("Maximum value in Array=", array_max)
print("Minimum value in Array=", array_min)

Array.reverse()
print("Reversed Array",Array)

start_index = int(input("Enter the start index for slicing:"))
end_index = int(input("Enter the end index for slicing:"))
subarray = Array[start_index:end_index]
print("SubArray=", subarray)

