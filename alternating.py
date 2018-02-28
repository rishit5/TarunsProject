def alternating(data):
    for i in range(1, len(data)-1):
        if ((data[i] >= data [i+1]) and (data[i] <= data[i-1])):
            return False
        if ((data[i] <= data[i+1]) and (data[i] >= data[i-1])):
            return False
    return True

if(alternating([3, 2, 1, 3, 5])):
    print 'True'
else:
    print 'False'
 