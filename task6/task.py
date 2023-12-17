import json

def task(range1, range2, range3):
    r1 = json.loads(range1)
    r2 = json.loads(range2)
    r3 = json.loads(range3)

    size = len(r1)
    sums = []
    for i in range(size):
        isum = 0
        isum += r1.index(f'O{i+1}')
        isum += r2.index(f'O{i+1}')
        isum += r3.index(f'O{i+1}')
        sums.append(isum)
    Dmax_sums = []
    for i in range(size):
        Dmax_sums.append(3*(i+1))
    average = sum(sums)/size
    D = sum([(i - average)**2 for i in sums])/(size-1)
    Dmax = sum([(i - average)**2 for i in Dmax_sums])/(size-1)
    return round(D/Dmax, 2)
    
range1 = '["O1","O2","O3"]'
range2 = '["O1","O3","O2"]'
range3 = '["O1","O3","O2"]'
print(task(range1, range2, range3))
