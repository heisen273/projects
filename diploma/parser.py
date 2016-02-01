import os.path
import sys, time
import re
from datetime import datetime
import datetime
from prettytable import PrettyTable

print 'Input must fit format /path/to/file.txt'
path = raw_input('Specify path to *.txt: ')
f = open(path, 'r')
row = f.read()
rows = (re.sub("WHERE.*", '', line) for line in row.splitlines())
row = '\n'.join(rows)
select = re.findall(r"\((.*?)\)", row)
f.close()

buff = []

for item in select:
    item = item.replace("'", '')
    lst = item.split(", ")
    frm = lst[0]
    to = lst[1]
    lst[0] = frm[:19]
    lst[1] = to[:19]
    if lst[8] == '{}':
        lst[8] = 'NULL'
    else:
        lst[8] = 'client'

    if lst[9] == '{}':
        lst[9] = 'NULL'
    else:
        lst[9] = 'account'

    if lst[10] == 'NULL':
        lst[10] = 'NULL'
    else:
        lst[10] = 'code'

    if lst[11] == 'NULL':
        lst[11] = 'NULL'
    else:
        lst[11] = 'code_name'
    FMT = '%Y-%m-%d %H:%M:%S'
    delta = str(
        datetime.datetime.strptime(lst[1], FMT) - datetime.datetime.strptime(lst[0], FMT) + datetime.timedelta(0, 1))
    parsed = []

    parsed.append(lst[4])  # GROUP_BY
    parsed.append(lst[8])  # CLIENT
    parsed.append(lst[9])  # ACCOUNT
    parsed.append(lst[10])  # CODE
    parsed.append(lst[11])  # CODE_NAME
    parsed.append(delta)  # TIME_FRAME
    buff.append(parsed)
############BUFF = [GROUP_BY, CLIENT, ACCOUNT, CODE, CODE_NAME, TIME_FRAME]

unique = []
unique_time = []

for element in buff:

    interval = element.pop()

    if element not in unique:
        unique.append(element)
        unique_time.append({interval: 1})
    elif element in unique:
        temp_dic = unique_time[unique.index(element)]
        if interval in temp_dic.keys():
            temp_dic[interval] += 1
        else:
            temp_dic[interval] = 1

count_sum = []

for item in unique_time:
    sum = 0
    for key in item.keys():
        sum += item[key]
    count_sum.append(sum)

table_sum = PrettyTable(['Group By', 'Query', 'Interval', 'Total'], sortby='Total', reversesort=True)

for element in unique:
    table_sum.add_row(
            [[element[0]], [element[1], element[2], element[3], element[4]], unique_time[unique.index(element)],
             count_sum[unique.index(element)]])

print table_sum
