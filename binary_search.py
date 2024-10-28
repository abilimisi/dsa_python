#binary search - o(logn)

def binary_search(arr,target):
    
    mid = 0
    low = 0
    high = len(arr)-1
    #step = 0

    while low <= high:
        
        #step+=1
        mid = (low+high)//2
        
        if arr[mid] == target:
            #print(step)
            return mid
        
        elif arr[mid] < target:
            low = mid+1

        elif arr[mid] > target:
            high = mid-1

        
    return -1


arr = [1, 2, 4, 7, 9]
target = 9

result = binary_search(arr,target)

if result != -1:
    print(f"number found at index : {result}")
else:
    print("number not found")
