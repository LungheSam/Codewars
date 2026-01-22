import numpy as np

# def is_sator_square(tablet):

#     #  <----  hajime!
#     column_transpose=[]
    
#     validation=True
#     for row in range(len(tablet)):
#         # print("row:",tablet[row])
#         # print("row_count:",tablet.count(tablet[row]))
#         # tablet_filtered=list(filter(lambda x: x != tablet[row], tablet))
#         # print(tablet_filtered)
#         if list(reversed(tablet[row])) in tablet:
#             # validation=True
#             continue
#         else:
#             # validation=False
#             return False
    
#     column_transpose=numpy.array(tablet)
#     column_transpose=column_transpose.T.tolist()
#     for col in range(len(column_transpose)):
#         if list(reversed(column_transpose[col])) in column_transpose:
#             # validation=True
#             continue
#         else:
#             return False
#     return True

def is_sator_square(tablet):
    # Convert to numpy array for easy transposition
    arr = np.array(tablet)
    rows = tablet
    cols = arr.T.tolist()
    
    n = len(tablet)
    
    for i in range(n):
        # 1. Row must read the same as the corresponding Column
        if rows[i] != cols[i]:
            return False
            
        # 2. Row must read the same backwards as the corresponding Row from the bottom
        # (e.g., Row 0 forward == Row n-1 backward)
        if rows[i] != list(reversed(rows[n - 1 - i])):
            return False
            
        # 3. Column must read the same backwards as the corresponding Column from the right
        if cols[i] != list(reversed(cols[n - 1 - i])):
            return False

    return True
        
square= [['T', 'E', 'N'],
            ['E', 'Y', 'E'],
                 ['N', 'E', 'T']]
sq2=[['M','P', 'K', 'N', 'F'],
['M', 'L','L', 'C','N'],
['K','L', 'U', 'L', 'K'],
['N', 'C', 'L', 'L', 'M'],
['F', 'N', 'K', 'P', 'M']]
print(is_sator_square(sq2))