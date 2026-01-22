def sum_n(n):
    s=(n*(n+1))//2
    return s 

def sum_of_sums(n):
    z=(n*(n+1)*(n+2))//6
    x=sum_n(z)
    return x
print(sum_of_sums(3))