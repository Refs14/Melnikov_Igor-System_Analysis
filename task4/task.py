import numpy as np

def sort_pair(roll: list[list]) -> list[list]:
    print(len(roll))
    for i in range(len(roll)):
        for j in range(len(roll)):
            if(i < j and roll[i][0] > roll[j][0]):
                (roll[i], roll[j]) = (roll[j], roll[i])

    for i in range(len(roll)):
        for j in range(len(roll)):
            if(i < j and roll[i][1] > roll[j][1] and roll[i][0] == roll[j][0]):
                (roll[i], roll[j]) = (roll[j], roll[i])
    return roll

def rolls_to_chance2(roll: list[list]) -> list:
    roll = sort_pair(roll)
    chance = list()
    chance.append(0.0)
    point0 = roll[0][0]
    point1 = roll[0][1]
    for el in roll:
        if(el[0] == point0 and el[1] == point1):
            chance[len(chance)-1] +=1
        else:
            chance[len(chance)-1] /=36
            chance.append(1.0)
            point0 = el[0]
            point1 = el[1]
    chance[len(chance)-1] /=36
    return chance

def rolls_to_chance(roll: list) -> list:
    roll.sort()
    chance = list()
    chance.append(0.0)
    point = roll[0]
    for el in roll:
        if(el==point):
            chance[len(chance)-1] +=1
        else:
            chance[len(chance)-1] /=36
            chance.append(1.0)
            point = el
    chance[len(chance)-1] /=36
    return chance

def entropy(chance: list) -> float:
    H = 0.0
    for el in chance:
        if(el!=0):
            H -= el*np.log2(el)
    return H

def task():
    cube = (1, 2, 3, 4, 5, 6)

    muls = [0] * 36
    for el1 in cube:
        for el2 in cube:
            muls[(el1-1)*6+(el2-1)] = el1*el2
    mul_chance = rolls_to_chance(muls)

    entropy_mul = entropy(mul_chance)
    print(mul_chance)
    #print(entropy(mul_chance))

    sums = [0] * 36
    for el1 in cube:
        for el2 in cube:
            sums[(el1-1)*6+(el2-1)] = el1+el2
    sum_chance = rolls_to_chance(sums)
    entropy_sum = entropy(sum_chance)
    #print(sum_chance)
    #print(entropy(sum_chance))

    sum_mul = [[0, 0]]
    for i in range(35):
        sum_mul.append([0, 0])
    for el1 in cube:
        for el2 in cube:
            sum_mul[(el1-1)*6+(el2-1)][0] = el1+el2
            sum_mul[(el1-1)*6+(el2-1)][1] = el1*el2
    sum_mul_chance = rolls_to_chance2(sum_mul)
    entropy_sum_mul = entropy(sum_mul_chance)
    #print(sum_mul_chance)
    #print(entropy(sum_mul_chance))
    return [round (el, 2) for el in [entropy_sum_mul, 
                                     entropy_sum, 
                                     entropy_mul, 
                                     entropy_sum_mul - entropy_sum, 
                                     entropy_sum + entropy_mul - entropy_sum_mul ]]

entropy_list = task()
print("H(AB) = ", entropy_list[0])
print("H(A) = ", entropy_list[1])
print("H(B) = ", entropy_list[2])
print("H_A(B) = ", entropy_list[3])
print("I(A,B) = ", entropy_list[4])
