def solution(citations):
    citations.sort()
    datas = list(enumerate(citations))
    result = 0

    for index, data in datas:
        if len(datas) - index >= data:
            result = max(result, data)
        else:
            result = max(result, len(datas) - index)

    return result