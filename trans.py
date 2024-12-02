import csv

hashmap = {}

with open('dic.tsv') as file:
    tsv_reader = csv.reader(file, delimiter='\t')

for row in tsv_reader:
    # Assuming the first column is the key and the second column is the value
    key = row[0]
    value = row[1]

    hashmap[key] = value

    print(hashmap)
