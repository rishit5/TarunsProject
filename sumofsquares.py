import math
def sumofsquares(data):
    if(data > 0):
        for i in range(1, int(math.sqrt(data))+1):
            for j in range(i, int(math.sqrt(data))+1):
                if( (i*i + j*j) == data):
                    return True
    else:
        return False
    return False
if __name__ == "__main__":
    n = input()
    if (sumofsquares(n)):
        print 'true'
    else:
         print 'false'