def rotatelist(data1, data2):
    list = data1
    if data2 < 0:
        return list
    for i in range(data2):
        x = list[len(list)-1]
        temp1 = list[0]
        for j in range(len(list)-1):
            temp2 = list[j+1]
            list[j+1] = temp1
            temp1 = temp2
        data1[0] = x
    return list
if __name__ == "__main__":
    list = raw_input().split(' ')
    list = [int(num) for num in list]
    list = rotatelist(list, 12)
    print list
