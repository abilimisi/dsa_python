# def alternate_element_of_an_array(arr):
#     print(arr[::2])
#
# arr = [-1,2,3,4,5,6]
# alternate_element_of_an_array(arr)


# Time Complexity: O(n)
# Space Complexity: O(n) (creates one extra list)
#in slicing it creates one extra list so its better option to go with second ex


def alternate_element_of_an_array(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")

arr = [-1, 2, 3, 4, 5, 6]
alternate_element_of_an_array(arr)

# Time Complexity: O(n) (traverses the array once).
# Space Complexity: O(1) (no extra list created).