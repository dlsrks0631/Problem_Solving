def solution(participant, completion):
    hashTable = {}
    temp = 0
    
    for i in participant:
        hashTable[hash(i)] = i
        temp += hash(i)

    for j in completion:
        temp -= hash(j)

    return hashTable[temp]