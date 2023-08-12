while True:
    data = input()
    
    if data == "0":
        break
    
    answer = "no"

    if data == data[::-1]:
        answer = "yes"
    
    print(answer)