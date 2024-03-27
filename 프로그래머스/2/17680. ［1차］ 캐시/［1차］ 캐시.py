def solution(cacheSize, cities):
    # 이미 캐시에 들어와있는 데이터가 다시 들어오는 경우
    hit = 1

    # 들어오는 데이터가 캐시에 없는 경우
    miss = 5
        
    cache = []
    time = 0

    if cacheSize == 0:
        return miss * len(cities)
    else:
        for city in cities:
            city = city.lower()
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += miss
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += hit    
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))