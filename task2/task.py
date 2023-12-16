import csv

def count_parents(point, table, found):
    ans = []
    new_parents = []
    for i in range(len(found)):
        if(table[point][i] == -1 and found[i] == 0):
            new_parents.append(i)
            ans.append(i)
            found[i] = 1
    for el in new_parents:
        ans = ans + count_parents(el, table, found)
    return ans

def count_child(point, table, found):
    ans = []
    new_parents = []
    for i in range(len(found)):
        if(table[point][i] == 1 and found[i] == 0):
            new_parents.append(i)
            ans.append(i)
            found[i] = 1
    for el in new_parents:
        ans = ans + count_child(el, table, found)
    return ans



def task(data):
    size = max(max(int(x) for x in lst) for lst in data)
    table = [[0]*size]
    for i in range(1, size):
          table.append([0]*5)
    for i in range(len(data)):
          table[data[i][0]-1][data[i][1]-1] = 1
          table[data[i][1]-1][data[i][0]-1] = -1
    answer = [[0]*5]
    for i in range(1, size):
          answer.append([0]*5)
    for i in range(size):
        #непросредственное управление
        count = 0
        for j in range(size):
            if(table[i][j] == 1):
                count += 1
        answer[i][0] = count
        #непросредственное подчинение
        count = 0
        for j in range(size):
            if(table[i][j] == -1):
                count += 1
        answer[i][1] = count
        #соподчинение
        count = 0
        for j in range(size):
            if(table[i][j] == -1):
                for k in range(size):
                     if(table[k][j] == -1 and k!=i):
                          count += 1
        answer[i][4] = count

        for j in range(size):
            #опосредованое подчинение
            answer[i][3] = len(count_parents(i, table, [0]*5)) - answer[i][1]
            #опосредованое управление
            answer[i][2] = len(count_child(i, table, [0]*5)) - answer[i][0]
    return answer
        

with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        data = [[int(x) for x in lst] for lst in data]
        answer = task(data)
        for row in answer:
            print(row)
