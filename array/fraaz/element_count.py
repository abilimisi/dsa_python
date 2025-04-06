def element_count(arr,target):
    count = 0
    for i in arr:
        if target == i:
            count+=1
    print(count)

arr = [1,2,3,4,2,5,6]
target = 2
element_count(arr,target)
