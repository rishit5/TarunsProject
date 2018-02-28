def ascending(data):
    for i in range(len(data)-1):
        if (data[i] > data[i+1]):
            return False
    return True 

if(ascending([7, 18, 17, 19])):
    print 'True'
else:
    print 'False'
