x = []
result=[]
for i in range(0,999999):
    x.append('%06d'%i)
for item in x:
    if sum([int(item[0]),int(item[1]), int(item[2])]) == sum([int(item[3]), int(item[4]), int(item[5])]):
        result.append(item)
for item in result:
    print item
print len(x), ' tickets total'
print len(result), ' is lucky tickets'
