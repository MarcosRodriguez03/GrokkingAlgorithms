arr = [3, 7, 10, 14, 18, 25]

def seartch(arr, target):
    low = 0 
    high = len(arr) - 1
    mid = (high + low) // 2
    while low <= high:
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            high = mid - 1
            mid = (high + low) // 2
        elif(arr[mid] < target):
            low = mid + 1
            mid = (high + low) // 2
    
print(seartch(arr, 7))



