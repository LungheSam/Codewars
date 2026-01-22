def find_even_index(arr):
    print(arr)
    for i in range(len(arr)):
        print("index:",i)
        left_sum=sum(arr[:i])
        print("left_sum=",left_sum)
        right_sum=sum(arr[i+1:])
        print("right_sum=",right_sum)
        if left_sum==right_sum:
            print(i)
            return i
    print("-1")
    return -1

find_even_index([10,-10])