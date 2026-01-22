def delete_nth(order,max_e):
    order_list=[]
    # element_to_delete=[]
    counts={}
    # for i in range(len(order)):
    #     # print(i,":",order.count(i),":find=>",order.index(i))
    #     occurance=order.count(order[i])
    #     index=i
    #     order_list.append((order[i],occurance,index))
    #     if occurance>max_e:
    #         element_to_delete.append((order[i],occurance,index))
    # dict_to_delete={}
    # for k,l,m in element_to_delete:
    #     if k in dict_to_delete.keys():
    #         dict_to_delete[k].append(m)
    #     else:
    #         dict_to_delete[k]=[]
    #         dict_to_delete[k].append(m)
    # for el in dict_to_delete.keys():
    #     while(len(dict_to_delete[el])>max_e):
    #         i_del=dict_to_delete[el].pop()
    #         del order[i_del]

    # print(dict_to_delete)
    # print(order_list)
    # print(element_to_delete)
    for el in order:
        current_count=counts.get(el,0)
        print(current_count)
        if current_count<max_e:
            order_list.append(el)
            counts[el]=current_count+1
    # print(counts)
    # print(order_list)
    # print(order)
    
    return order

delete_nth([20,37,20,21],1)