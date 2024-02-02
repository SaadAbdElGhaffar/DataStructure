def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
        return length + 1
    return length

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
        return length - 1
    return length

def insertMiddle(arr, n, i, length, capacity):
    if length < capacity:
        for index in range(length - 1, i - 1, -1):
            arr[index + 1] = arr[index]
        arr[i] = n
        return length + 1
    return length

def removeMiddle(arr, i, length):
    if length > 0:
        for index in range(i, length):
            arr[index] = arr[index + 1]
        arr[length - 1] = 0
        return length - 1
    return length

def printArray(arr, length):
    for index in range(length):
        print(arr[index])

size = int(input("Enter size of list\n"))
arr = [0] * size
length = 0

for index in range(size):
    n = int(input(f"Enter the element of {index + 1}\n"))
    length = insertEnd(arr, n, length, size)

printArray(arr, size)
print("removeMiddle")
length=removeMiddle(arr,length,size)
printArray(arr,length)
print("insertMiddle")
length=insertMiddle(arr,3,2,length,size)
printArray(arr,length)