def rem_ele_at_pos(array,pos):
    for i in range(pos,len(array)-1):
        array[i] = array[i+1]

array = [10,12,23,34,26]
pos = 2
rem_ele_at_pos(array,pos)
for i in range(len(array)-1):
    print(array[i],end=" ")