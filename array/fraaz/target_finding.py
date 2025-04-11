def find_terget(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j] == target):
                return True #use return not break
    else:
        return False

nums = [1,2,4,5,6]
target = 11

res = find_terget(nums,target)

if(res):
    print("Found")
else:
    print("Not Found")
