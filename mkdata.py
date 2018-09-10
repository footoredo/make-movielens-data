#!/usr/bin/python
import sys
from datetime import datetime, tzinfo, timedelta

if len(sys.argv) < 6:
    print('Usage: ./mkdata.py user.data user.feature \
            item.data item.feature all.feature')
    exit(-1)

users = {}
with open(sys.argv[1]) as user_data:
    for line in user_data:
        data = line.strip().split('|')
        users[int(data[0])] = map(int, data[1:])

items = {}
with open(sys.argv[3]) as item_data:
    for line in item_data:
        data = line.strip().split('|')
        items[int(data[0])] = map(int, data[1:])

features = []

cnt_user_features = 0
with open(sys.argv[2]) as user_feature:
    for feature in user_feature.readline().split(' '):
        name, cnt = tuple(feature.split(':'))
        features.append((name, int(cnt)))
        cnt_user_features += int(cnt)

cnt_item_features = 0
with open(sys.argv[4]) as item_feature:
    for feature in item_feature.readline().split(' '):
        name, cnt = tuple(feature.split(':'))
        features.append((name, int(cnt)))
        cnt_item_features += int(cnt)

features.append(('hour', 24))
features.append(('day', 31))
features.append(('weekday', 7))
features.append(('month', 12))
features.append(('year', 20))

fin = sys.stdin
fout = sys.stdout

for line in fin:
    data = line.strip().split('\t')
    feature_user = users[int(data[0])]
    feature_item = items[int(data[1])]
    dt = datetime.fromtimestamp(int(data[2]))
    dt -= timedelta(hours = 6)

    def print_feature(feature):
        fout.write(' ')
        fout.write(str(feature))
        fout.write(':1')

    fout.write(data[2])
    for feature in feature_user:
        print_feature(feature)

    cnt = cnt_user_features
    for feature in feature_item:
        print_feature(cnt + feature)

    cnt += cnt_item_features
    print_feature(cnt + dt.hour)
    cnt += 24
    print_feature(cnt + dt.day - 1)
    cnt += 31
    print_feature(cnt + dt.weekday())
    cnt += 7
    print_feature(cnt + dt.month - 1)
    cnt += 12
    print_feature(cnt + dt.year - 1990)
    
    fout.write('\n')

with open(sys.argv[5], "w") as ffeat:
    ffeat.write(' '.join(map(lambda (name, cnt): 
        name + ":" + str(cnt), features)))
