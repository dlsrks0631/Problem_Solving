def solution(s):
    data = []
    
    for st in s:
        if st == "(":
            data.append(st)
        elif data and data[0] == "(" and st == ")":
            data.pop()
        else:
            data.append(st)

    if not data:
        return True
    else:
        return False