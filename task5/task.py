import numpy as np

#преобразование ранжировки из json строки в двумерный list
def str_to_list2(json_str: str):
    json_str = str(json_str[1:-1])
    spl1 = json_str.split('[')
    json_list = []
    for el in spl1:
        for i in range(len(el.split(']'))):
            json_list.append(el.split(']')[i])
    list2 = [[]]
    for i in range(len(json_list)):
        if(i%2==1):
            list2.append(list(map(int, json_list[i].split('"')[1::2])))
        else:
            for j in range(len(json_list[i].split('"'))):
                if(j%2==1):
                    list2.append([int(json_list[i].split('"')[j])])
    list2 = list2[1::1]
    return list2

def at(element: int, list1: list[list]):
    index = -1
    for i in range(len(list1)):
        for el in list1[i]:
            if(el == element):
                return i
    return index

#матрица отношений по ранжировке
def matrix(a_range):
    table = np.zeros((10, 10), dtype=int)
    for i in range(10):
        for j in range(10):
            if(at(i+1, a_range) <= at(j+1, a_range)):
                table[i][j] = 1
    return table

#поэлементное перемножение матриц
def AND_matrix(matrix1, matrix2):
    res_matrix = np.zeros((len(matrix1), len(matrix1[0])), dtype=int)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            res_matrix[i][j]= matrix1[i][j]*matrix2[i][j]
    return res_matrix

#поэлементное cложение матриц
def OR_matrix(matrix1, matrix2):
    res_matrix = np.zeros((len(matrix1), len(matrix1[0])), dtype=int)

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            res_matrix[i][j]= max(matrix1[i][j], matrix2[i][j])
    return res_matrix

#поиск ядра противоречий по 2 ранжировкам
def conflict_core(a_range, b_range):
    m1 = matrix(a_range)
    m2 = matrix(b_range)
    AND_m = AND_matrix(m1, m2)
    AND_T_m = np.transpose(AND_m)

    OR_m = OR_matrix(AND_m, AND_T_m)
    return OR_m

#согласование ранжировок
def create_range(core, a_range, b_range):
    m1 = matrix(a_range)
    m2 = matrix(b_range)
    similar = []
    found = []
    for i in range(10):
        if(i+1 not in found):
            similar.append([i+1])
            found.append([i+1])
            for j in range(10):
                if(core[i][j] == 0):
                    similar[len(similar)-1].append(j+1)
                    found.append(j+1)
                  
    #ранжировка в формате: ранжировка 1, ранжировка 2, ядро противоречий, номер
    comparisions = []
    for i in range(10):
        comparisions.append([sum(m1[i]), sum(m2[i]), at(i+1, similar), i+1])
      
    #отсортировано по 1 ранжировке и при равных по 2 ранжировке
    for i in range(10):
        for j in range(10):
            if(i < j and comparisions[i][0] < comparisions[j][0]):
                (comparisions[i], comparisions[j]) = (comparisions[j], comparisions[i])
            if(i < j and comparisions[i][0] == comparisions[j][0] and comparisions[i][1] < comparisions[j][1]):
                (comparisions[i], comparisions[j]) = (comparisions[j], comparisions[i])
        
    result = []
    found = []
    for i in range(10):
        if(i not in found):
            #добавить первый по сортировке элемент (только первая итерация)
            if(i==0):
                result.append([comparisions[i][3]])
            #Добавить элемент в новый кластер
            elif(comparisions[i][1] < comparisions[i-1][1] or comparisions[i][0] < comparisions[i-1][0]):
                result.append([comparisions[i][3]])
            #Добавить элемент в последний кластер
            else:
                result[len(result)-1].append(comparisions[i][3])
            #учесть элемент как добавленный
            found.append(i)
            #добавление элементов из того же кластера ядра противоречий
            for j in range(10):
                if(i!=j and comparisions[i][2] == comparisions[j][2] and j not in found):
                    result[len(result)-1].append(comparisions[j][3])
                    found.append(j)
    return result


def task(a_input, b_input):
    a_range = str_to_list2(a_input)
    b_range = str_to_list2(b_input)
    core1 = conflict_core(a_range, b_range)
    final_range1 = create_range(core1, a_range, b_range)
    print(final_range1)

a_input = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
b_input = '[["1", "2"],["3","4","5"],"6","7","9",["8", "10"]]'
c_input = '["3",["1","4"],"2","6",["5","7","8"],["9", "10"]]'

task(a_input, b_input)
task(a_input, c_input)
