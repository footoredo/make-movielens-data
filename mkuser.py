#!/usr/bin/python
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: ./mkuser.py feature-user.txt")

fin = sys.stdin
fout = sys.stdout

users = []
ages = []
occupations = {}
cnt_occupations = 0
zipcodes = {}
cnt_zipcodes = 0

for line in fin:
    fields = line.split('|')
    i, age, gender, occupation, zipcode = tuple(fields)

    user = {}
    user["id"] = int(i)
    user["age"] = int(age)
    ages.append(int(age))
    if not occupation in occupations:
        occupations[occupation] = cnt_occupations
        cnt_occupations += 1
    user["occupation"] = occupations[occupation]
    if not zipcode in zipcodes:
        zipcodes[zipcode] = cnt_zipcodes
        cnt_zipcodes += 1
    user["zipcode"] = zipcodes[zipcode]

    users.append(user)

min_age = min(ages)
cnt_ages = max(ages) - min_age + 1
for user in users:
    features = []
    features.append(user["id"])
    features.append(user["age"] - min_age)
    features.append(user["occupation"] + cnt_ages)
    features.append(user["zipcode"] + cnt_ages + cnt_occupations)

    fout.write('|'.join(map(str, features)) + '\n')

features = [('age', cnt_ages), ('occupation', cnt_occupations), 
        ('zipcode', cnt_zipcodes)]
with open(sys.argv[1], "w") as ffeat:
    ffeat.write(' '.join(map(lambda (name, cnt): 
        name + ":" + str(cnt), features)))
