# C:/Users/um006/Anaconda3/python.exe
n = int(input())
res = []
for _ in range(n):
    # 메모리크기, 코드길이, 입력의 크기
    m, c, i = map(int, input().split()) 
    arr = [0] * m
    code = list(str(input())) # +, - , . , > . <
    input_ = list(str(input())) # 문자열

    # [ 이랑 ] 위치 인덱스찾기.
    index_map, stk, idx = dict(), [], 0
    while True:
        if idx == c:
            break
        if code[idx] == '[':
            stk.append(idx)
        elif code[idx] == ']':
            temp = stk.pop()
            index_map[idx], index_map[temp] = temp, idx
        idx += 1
    ptr, code_idx, input_idx, max_oper_idx = 0, 0, 0, 0 # 데이터를 저장하는 ptr, 명령 프로그램 idx
    for _ in range(50000000): # +[+[-]]
        command = code[code_idx]
        if command == '-':
            arr[ptr] = 255 if arr[ptr] == 0 else arr[ptr] - 1
        elif command == '+':
            arr[ptr] = 0 if arr[ptr] == 255 else arr[ptr] + 1
        elif command == '.':
            pass
        elif command == ',':
            if input_idx == i:
                arr[ptr] = 255
            else:
                arr[ptr] = ord(input_[input_idx])
                input_idx += 1
        elif command == '<':
            ptr -= 1
            if ptr < 0:
                ptr = m-1
        elif command == '>':
            ptr += 1
            if ptr == m:
                ptr = 0
        elif command == '[':
            if arr[ptr] == 0:
                code_idx = index_map[code_idx]
        elif command == ']':
            if arr[ptr] != 0:
                code_idx = index_map[code_idx]
        code_idx += 1
        max_oper_idx = code_idx if code_idx > max_oper_idx else max_oper_idx
        
        # 코드 모두 수행한 결과이면.
        if code_idx == c:
            res.append("Terminates")
            break
    if code_idx != c:
        res.append("Loops %d %d" % (index_map[max_oper_idx], max_oper_idx))

for response in res:
    print(response)