def hansu(x):
    x = str(x)
    count = 0
    list = []
    result = True
    
    while count != len(x)-1:
            difference = int(x[i])-int(x[i+1])
            list.append(difference)
            count += 1
    setlist = set(list)
    if len(setlist) == 0 or len(setlist) == 1:
        return True
    else:
        return False
            
    return result

n = int(input())
TFlist = []
for i in range(n):
    TFlist.append(hansu(i+1))
ans = TFlist.count(True)
print(ans)
