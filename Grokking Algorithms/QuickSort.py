def quicksort (arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        for i in arr[1:]: 
            if i < pivot:
                less.append(i)

        greater = []
        for i in arr[1:]:
            if i > pivot:
                greater.append(i)

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10,5,2,3]))


def quicksort2(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        less = []
        greater = []

        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
        return quicksort2(less) + [pivot] + quicksort2(greater)
    
print(quicksort2([10,5,2,3]))
        