def fruits(tuple_of_fruits):
    my_dic = {}
    for i in tuple_of_fruits:
        if i['shape'] == 'sphere' and (i['mass'] >= 300 or i['mass'] <= 600) and (
                i['volume'] >= 100 or i['volume'] <= 500):
            if i['name'] not in my_dic:
                my_dic[i['name']] = 1
            else:
                my_dic[i['name']] += 1
    return my_dic
