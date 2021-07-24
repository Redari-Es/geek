import csv

csvfile = open('csv_test.csv', 'r')
#以列表形式输出
reader = csv.reader(csvfile)
for row in reader:
    if '小p' in row:
        print(row)
#以字典形式输出，第一行作为字典的键
reader = csv.DictReader(csvfile)
for row in reader:
    if row['姓名'] == '小p':
        print(row)
