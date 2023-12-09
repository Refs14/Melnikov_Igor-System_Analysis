import csv

file_name = 'data.csv'
in_ = input().split(' ')
a = int(in_[0])
b = int(in_[1])


with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
    print(data[a][b])
