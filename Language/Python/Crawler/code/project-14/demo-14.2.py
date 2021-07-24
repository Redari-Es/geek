import csv

csvfile = open('csv_test.csv', 'r')
#以列表形式输出
reader = csv.reader(csvfile)
#以字典形式输出，第一行作为字典的键
#reader=csv.DictReader(csvfile)
rows = [row for row in reader]
print(rows)
