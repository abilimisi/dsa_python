#linear search - 0(n)

def linear_search(arr,target):
    #steps  = 0
    for index in range(len(arr)):
        
        #steps+=1
        
        if arr[index] == target:
            #print(steps)
            return index
    else:
        return -1
    
        
arr = [1,2,4,7,9]
target = 9

result = linear_search(arr,target)

if result != -1:
    print(f"number found at index : {result}")
else:
    print("number not found")

