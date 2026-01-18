def order(sentence):
    if sentence=="":
        return ""
    sentence_list=sentence.split(" ")
    sentence_int_list=[]
    for element in sentence_list:
        for i in list(element):
            if i in '123456789':
                sentence_int_list.append(i)

               
    
    sentence_int_list=list(map(lambda x:int(x),sentence_int_list))
    sentence_int_list=sorted(sentence_int_list)
    print(sentence_int_list)
    last_list=[]
    for i in sentence_int_list:
        for k in sentence_list:
            if str(i) in k:
                last_list.append(k)
    print(last_list)
    return " ".join(last_list)

print(order("4of Fo1r pe6ople g3ood th5e the2"))