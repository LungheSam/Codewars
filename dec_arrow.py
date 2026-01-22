def moveup(numbers,i):
    for row in range(len(numbers)):
        for col in range(len(numbers[0])):
            if numbers[row][col]==i:
                if row-1 <0:
                    return 'X'
                return numbers[row-1][col]
def movedown(numbers,i):
    for row in range(len(numbers)):
        for col in range(len(numbers[0])):
            if numbers[row][col]==i:
                if row+1 >=len(numbers):
                    return 'X'
                return numbers[row+1][col]
            
def moveleft(numbers,i):
    for row in range(len(numbers)):
        for col in range(len(numbers[0])):
            if numbers[row][col]==i:
                if col-1 <0:
                    return 'X'
                return numbers[row][col-1]

def moveright(numbers,i):
    for row in range(len(numbers)):
        for col in range(len(numbers[0])):
            if numbers[row][col]==i:
                if col+1>=len(numbers[0]):
                    return 'X'
                return numbers[row][col+1]
def dec_arrow_pin_code(arrow_str):
    pin_code=[]
    numbers=[['7','8','9'],
             ['4','5','6'],
             ['1','2','3'],
             ['0','X','X']]
    arrow_array=list(arrow_str)
    pin_code.append(arrow_array[0])
    # print(pin_code)
    for i in range(len(arrow_str)-1):
        if arrow_array[i] == 0:
            if arrow_array[i+1] in "→←↓":
                return []

        if arrow_array[i+1]=="←":
            last_el=pin_code[-1]
            pin_code.append(moveleft(numbers,last_el))
        elif arrow_array[i+1]=="→":
            last_el=pin_code[-1]
            pin_code.append(moveright(numbers,last_el))
        if arrow_array[i+1]=="↑":
            last_el=pin_code[-1]
            pin_code.append(moveup(numbers,last_el))
        elif arrow_array[i+1]=="↓":
            last_el=pin_code[-1]
            pin_code.append(movedown(numbers,last_el))
        if arrow_array[i+1]=='*':
            el_to_rep=pin_code[-1]
            for i in range(int(arrow_array[i+2])):
                pin_code.append(el_to_rep)
            # repeat_previous(numbers,el_to_rep)
    print(arrow_str)
    print(pin_code)
    if 'X' in pin_code:
        return []
    
    pin_code=[int(x) for x in pin_code]
    return pin_code

dec_arrow_pin_code('0↑↑↑')
dec_arrow_pin_code('0↑↑↑↑')
dec_arrow_pin_code('5←*2↓→')
dec_arrow_pin_code('9↓↓←←↓*3')