def snail(snail_map):
    if len(snail_map[0])==0:
        return []
    rows=[x for x in range(len(snail_map))]
    cols=[x for x in range(len(snail_map[0]))]
    first_row_index=0
    first_col_index=0
    last_row_index=len(rows)-1
    last_col_index=len(cols)-1
    result=[]
    i=0
    while (first_row_index<last_row_index):
        # print("-------------------------------------------")
        # print("Rotation:",first_row_index+1)
        # print("-------------------------------------------")
        # print("First Row Index:",first_row_index)
        # print("First Column Index:",first_col_index)
        # print("Last Row Index:",last_row_index)
        # print("Last Column Index:",last_col_index)
        # print("--------------------------------------------")

        for col in range(first_col_index,last_col_index+1):
            result.append(snail_map[first_row_index][col])
        for row in range(first_row_index+1,last_row_index+1):
            result.append(snail_map[row][last_col_index])
        for col in range(last_col_index-1,first_col_index-1,-1):
            result.append(snail_map[last_row_index][col])
        for row in range(last_row_index-1,first_row_index,-1):
            result.append(snail_map[row][first_col_index])
        last_col_index-=1
        last_row_index-=1
        first_col_index+=1
        first_row_index+=1
        # print(result)
    if len(snail_map[0])%2 !=0:
        result.append(snail_map[first_row_index][first_col_index])
    # print(result)
    return result
    

def execute(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("Result:",snail(arr))
array1 = [[1,2,3,0],
         [4,5,6,0],
         [7,8,9,0],
         [7,8,9,0]]

array2=[[1,2,3],
        [4,5,6],
        [7,8,9]]
array3 = [[1,2,3,0,1],
         [4,5,6,0,1],
         [7,8,9,0,1],
         [7,8,9,0,1],
         [4,5,6,0,1]]
# expected = [1,2,3,6,9,8,7,4,5]
array4=[[1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]
execute(array4)
# [1, 2, 3, 0, 1, 1, 1, 1, 1, 0, 6, 5, 4, 7, 7, 4, 5, 6, 0, 0, 0, 9, 8, 8, 9]