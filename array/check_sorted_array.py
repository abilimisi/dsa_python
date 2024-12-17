def sorted_array(sorted_arr):
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            return False
    else:
        return True


arr = [1, 2, 2, 4, 7, 9]
if sorted_array(arr):
    print("True")
else:
    print("false")
