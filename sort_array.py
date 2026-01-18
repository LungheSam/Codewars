#sort only the odd numbers 
def sort_array(array):
    print("Before Sorting:",array)
    all_odds_array=[]
    keep_index=[]
    keep_element=[]
    for a in array:
        if a%2 != 0:
            all_odds_array.append(a)
    if len(all_odds_array)==len(array):
        return sorted(array)
    for i in range(len(array)):
        if array[i]%2 !=0:
            keep_element.append(array[i])
            keep_index.append(i)
    keep_element=sorted(keep_element)
    e=0
    for k in keep_index:
        while (e<len(keep_element)):
            array[k]=keep_element[e]
            e+=1
            break
    # print(keep_element)
    # print(keep_index)
    # print(array)
    return array

my_array=[9,20,1,18,3,11,60]
print("After Sorting:",sort_array(my_array))
