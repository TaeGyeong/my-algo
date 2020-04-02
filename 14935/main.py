def FA(s):
    return str(int(s[0]) * len(s))

a = str(input())
count = 0
temp = -1
while True:
    count += 1
    temp = FA(a)
    if a == temp:
        print('FA')
        break
    else:
        a = temp
        if count == 100000000:
            print('NFA')
            break
    
    