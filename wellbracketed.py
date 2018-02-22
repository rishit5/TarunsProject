def wellbracketed(data):
    depth = 0
    for ch in data:
        if ch == '(':
            depth = depth+1
        if ch == ')':
            depth = depth-1
    if depth == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    string = raw_input()
    if(wellbracketed(string)):
        print 'true'
    else:
        print 'false'