import os.path
import sys,time
import re
print("Input must fit format /path/to/file.txt")
path=raw_input("Path to *.txt: ")
tmp = []
def antohin_parser(path):
    iterator = 0
    f = open(path, 'r')
    row = f.read()
    query = re.findall(r"\((.*?)\)", row)
    f.close()
    for item in query:
        item = item.replace("'",'')
        tmp.append(item)
        for i in tmp:
            i = i.split(', ')
            if i[4] == 'code_name':
                iterator += 1
            elif i[4] == 'code_name,days':
        
        print iteratorn
        print len(query)
antohin_parser(path)







lets say I have alot of lines which in a list
'2015....  '
'2014....  '
and so on 

for every element of list:
    we replace element with  ("'", '')

    i want to put first replaced element into TMP
    then split TMP by (', ')
    Then if TMP[4] <> NULL:
        i remember TMP[4] value and +1 my iterator
    After i go to my second replaced element and also if TMP[4] <> NULL:
        i check if my previous TMP[4] value is different from current and if it is - i increment my iterator
        elif it is different:
            i increment my iterator2 
    keep going untill the end
in the end i must get something like this:

    TMP[4]* value: iterator    -- for each unique TMP[4]
