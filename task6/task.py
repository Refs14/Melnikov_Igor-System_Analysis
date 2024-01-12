import json

def task(range1, range2, range3):
    r1 = json.loads(range1)
    r2 = json.loads(range2)
    r3 = json.loads(range3)
    rank1 = [int(el[1]) for el in r1]
    rank2 = [int(el[1]) for el in r2]
    rank3 = [int(el[1]) for el in r3]
    n = len(rank1)
    concordant = 0
    discordant = 0
    for i in range(n):
        for j in range(i+1, n):
            # Проверяем каждую пару элементов из ранжировок
            for rank in [rank1, rank2, rank3]:
                if (rank[i] < rank[j] and rank2[i] < rank2[j] and rank3[i] < rank3[j]) or (rank[i] > rank[j] and rank2[i] > rank2[j] and rank3[i] > rank3[j]):
                    # Если все три ранжировки согласованы (все три пары имеют одинаковый порядок)
                    concordant += 1
                else:
                    # В противном случае - несогласованные пары
                    discordant += 1
    # Коэффициент Кендалла
    kendall_tau = (concordant - discordant) / (concordant + discordant)
    return kendall_tau

# Пример использования
range1 = '["O1","O2","O3"]'
range2 = '["O1","O3","O2"]'
range3 = '["O1","O3","O2"]'
print("Коэффициент Кендалла:", task(range1, range2, range3))

range1 = '["O1","O2","O3"]'
range2 = '["O1","O2","O3"]'
range3 = '["O1","O2","O3"]'
print("Коэффициент Кендалла:", task(range1, range2, range3))
