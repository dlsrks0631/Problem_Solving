def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    result = [0] * 3

    answers = list(enumerate(answers))
    answer = []

    for index, data in answers:
        if p1[index % 5] == data:
            result[0] += 1
        if p2[index % 8] == data:
            result[1] += 1
        if p3[index % 10] == data:
            result[2] += 1
    
    for i in range (3):
        if result[i] == max(result):
            answer.append(i+1)
            
    return answer