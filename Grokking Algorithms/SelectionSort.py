# Given example of Selection Sort algorithm
arrExample = [6,4,7,3,5,8,]
newArr = []

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if(arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

for i in range(0, len(arrExample)):
    index = findsmallest(arrExample)
    newArr.append(arrExample.pop(index))
print(newArr)

# Swapping elements within the array
arr = [6,4,7,3,5,8,]
for i in range(0, len(arr)):
    index = i
    value = arr[i]

    for j in range(i, len(arr)):
        if (arr[j] < value):
            index = j 
            value = arr[j]

    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

print(arr)

