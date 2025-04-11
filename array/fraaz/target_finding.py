def find_terget(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j] == target):
                print("Found")
                return  #use return not break
    print("Not Found")

nums = [1,2,3,4,5,6]
target = 11

find_terget(nums,target)


