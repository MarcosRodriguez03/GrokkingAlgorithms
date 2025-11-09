def fact(num):

    # Base case
    if num <= 0:
        return 1
    # Recursive case
    else:
      return num * fact(num - 1 )

print(fact(5))

# after every recursive call, the return value will be added to the top of the stack until it reaches the base case
# it is important to return 1 in the base case becasue it will multiply by the previous value in the stack
# my error was returning num itself which was 0, this caused my result to be 0


#sum of array

# In this case i need to create a recursive function that will add the next number to the intial number 
# If this was a for loop I would create a total variable and add a new num after each iteration
# In recursion there isnt typcally a total variable since every call has its own scope
# base case: I can end the the recursive calls when it reaches the end of the array, but how do i know this. I need to keep track of the index somehow

# after asking claryfying questions I decdied to alter the array input each call
# new base case: When the length of the input array is 1, that means it is the last element

num_array = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

def sumArr(arr):
    if(len(arr) == 1):
        return arr[0]
 
    else:
        return arr[0] + sumArr(arr[1:])

print(sumArr(num_array))

# Similar to the sumArr excercise, I will alter the array input each call
# I will use the same same strategy of checking the base case: when len(arr) is 1
# since im not allowed to carry over an index variable, Ill check the first and second elements of the currecnt array.
# i will swap the highest value into the next position saving it from being deleted the next call

max_Array_Test = [4,3,2,1]

def max_Array(arr):
    if(len(arr) == 1):
        return arr[0]
    elif( arr[0] > arr[1]):
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
        return max_Array(arr[1:])
    else:
        return max_Array(arr[1:])

print(max_Array(max_Array_Test))



countingArr = [1,2,3,4,5,6,7]

def countArr(arr):
    if (len(arr) == 1):
        return 1
    else:
        return 1 + countArr(arr[1:])

print(countArr(countingArr))

def powerFunct(base, n):
    if(n == 0):
        return 1
    if(n <= 1):
        return base
    else:
        return base * powerFunct(base, n-1)

print(powerFunct(2,4))