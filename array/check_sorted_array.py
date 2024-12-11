def sorted_array(sorted_arr):
    for i in range(1,len(sorted_arr)):
        if sorted_arr[i-1] > sorted_arr[i]:
            return False
    else:
        return True

arr = [1, 2, 2, 4, 7, 9]
if(sorted_array(arr)):
    print("True")
else:
    print("false")


