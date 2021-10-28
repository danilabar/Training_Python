import csv

with open('files_8/test.csv', newline='', encoding='utf-8') as f:
    #reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    reader = csv.reader(f, delimiter=',')
    new_list = list(reader)


print(new_list)
