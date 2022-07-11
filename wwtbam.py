import random 
import sys
import xlrd
import csv

book = xlrd.open_workbook("test_qs.xls")
data = book.sheet_by_index(0)

questions = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: []
}


levels =  {1: '$100',
2: '$500',
3: '$1,000',
4: '$2,000',
5: '$4,000',
6: '$8,000',
7: '$16,000',
8: '$32,000' ,
9: '$64,000',
10: '$125,000',
11: '$250,000',
12: '$500,000',
13: '$1,000,000'}

used = []

with open('used.txt','r') as g:
    reader = csv.reader(g)
    for row in reader:
        item = row[0]
        used.append(item)


used = set(used)

#print(used)


for r in range(1, data.nrows):
    x = data.row(r)
    x = [y.value for y in x]
    level = x[0]
    questionid = x[1]
    if str(questionid) not in used: 
        q = x[3]
        choices = {'a': x[4], 'b': x[5], 'c': x[6], 'd': x[7]}
        answer = x[8]
        items =  {'id': questionid, 'q': q, 'choices': choices,
        'answer': answer}
        #print(items)
        thislist = questions[level]
        thislist.append(items)
        questions[level] = thislist

with open('used.txt','a') as f:
    writer = csv.writer(f)


    def askme(l):

        x = random.choice(questions[l])
        print(x['q'])
        for c in x['choices'].items():
            print(c[0], ": ", c[1])
        thisid = x['id']
        writer.writerow([thisid])
        answer = x['answer']
        print('\n')
        mychoice = input('FINAL ANSWER: ')
        if mychoice == answer:
            print('Correct!')
            print(' --------------------')
            print('\n')
            result = 'correct'
            return result
        else: 
            print('SORRY, YOU LOSE!')
            print(' --------------------')
            print('\n')
            result = 'incorrect'
        return result


    for l in range(1,14):
        amount = levels[l]
        print('\n')
        print("For " + amount + "...")
        print('\n')
        x = askme(l)
        if x == 'incorrect':
            break
        else:
            pass

f.close()




