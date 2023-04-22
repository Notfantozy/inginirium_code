while True:
    str = input('ctroka')
    for s in range(0,len(str),1):
        print(chr(ord(str[s]) + 3),end=',')
