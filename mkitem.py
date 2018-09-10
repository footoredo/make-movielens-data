#!/usr/bin/python
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: ./mkitem.py feature-item.txt")
    exit(-1)

fin = sys.stdin
fout = sys.stdout

features = [('release_day', 31), ('release_month', 12), 
        ('release_year', 100), ('genre', 19)]
with open(sys.argv[1], "w") as ffeat:
    ffeat.write(' '.join(map(lambda (name, cnt): 
        name + ":" + str(cnt), features)))

for line in fin:
    item = {}
    fields = line.strip().split('|')

    feat = [int(fields[0])]
    try:
        date = datetime.strptime(fields[2], "%d-%b-%Y")
        feat.append(date.day - 1)
        feat.append(date.month - 1 + 31)
        feat.append(date.year - 1900 + 31 + 12)
    except ValueError:
        pass
    genres = filter(lambda (i, x): x == "1", enumerate(fields[-19:]))
    feat += list(map(lambda (i, x): i + 31 + 12 + 100, genres))

    fout.write('|'.join(map(str, feat)) + '\n')

"""
min_year = min(years)
cnt_years = max(years) - min_year + 1
for item in items:
    features = []
    features.append(item["id"])
    if "date" in item:
        features.append(item["date"].day - 1)
        features.append(item["date"].month - 1 + 31)
        features.append(item["date"].year - min_year + 12 + 31)
    base = 12 + 31 + cnt_years
    features += list(map(lambda i: i + base, item["genres"]))
    fout.write('|'.join(map(str, features)) + '\n')
"""
