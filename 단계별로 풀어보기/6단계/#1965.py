def hansu(x):
    x = str(x)
    count = 1
    list = []
    result = True
    
    while count != len(x):
        for i in range(len(x)):
            difference = int(x[i])-int(x[i+1])
            list.append(difference)
            count += 1
    print(list)    
    for i in range(len(list)):
        if list[i] == list[i+1]:
            result = True
        else:
            result = False
            
    return result
