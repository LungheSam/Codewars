def in_array(array1, array2):
    # your code
    result=set([])
    for a1 in array1:
        for a2 in array2:
            if a1 in a2:
                result.add(a1)
    result=list(result)       
    return result