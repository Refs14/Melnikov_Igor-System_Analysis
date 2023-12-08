import numpy as np

def task(csv_str: str) -> float:
    return find_entropy(csv_str.split("\n"))

def find_entropy(data: list) -> float:
    H = 0.0
    n = len(data)
    for line in data:
        for el in line.split(","):
            s = float(int(el))/(n - 1)
            if(s!=0):
                H -= s*np.log2(s)
    return H

data = "2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1"
print(task(data))
