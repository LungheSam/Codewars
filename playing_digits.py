from math import floor
def dig_pow(n, p):
    # your code
    n_list=list(map(lambda x: int(x),list(str(n))))
    print(n_list)
    result=0
    for n_el in n_list:
        result+=n_el**p
        p+=1
    # print(result)
    k=result/n
    if (k-floor(k)) == 0.0:
        return int(k)
    else:
        return -1
print(dig_pow(89,1))