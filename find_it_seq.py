def find_it(seq):
    for i in seq:
        print(f"{i}:{seq.count(i)}")
        if seq.count(i) %2 != 0:
            odd_count=seq.count(i)
    return odd_count

find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])