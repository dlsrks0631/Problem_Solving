burgers = []
for _ in range(3): 
    burgers.append(int(input()))
    
drinks = []
for _ in range(2): 
    drinks.append(int(input()))

min_set = min(burgers) + min(drinks) - 50  
print(min_set)