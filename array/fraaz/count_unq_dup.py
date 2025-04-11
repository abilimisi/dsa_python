#here both are different problems
def count_unique_and_duplicates(nums):
    hash_table = [0] * 101

    for num in nums:
        hash_table[num] += 1
    unique_counts = 0
    duplicate_count = 0

    for freq in hash_table[1:]: #here we are ignoring 0,l bcz we are taking array starting with 1 in input
        if freq == 1:
            unique_counts += 1

        elif freq > 1:
            duplicate_count += freq-1
            # duplicate_count += 1


    print("unique :",unique_counts,"duplicate :",duplicate_count)
    print(hash_table)

nums = [1,4,5,4,6,7,4]   #here 4,4,4 so dup count is 2
count_unique_and_duplicates(nums)

#----------------------------------------------------------------
def counts_unique_and_duplicates(arr):
    dict_counting = {}
    unique_count = 0
    dup_count = 0

    for i in arr:
        if i in dict_counting:
            dict_counting[i]+=1
        else:
            dict_counting[i] = 1
    for value in dict_counting.values():
        if value == 1:
            unique_count+=1
        else:
            dup_count+=1
    print("unique :",unique_count,"duplicate :",dup_count)

arr = [2,7,9,10,2,7,12,17,7]
counts_unique_and_duplicates(arr)