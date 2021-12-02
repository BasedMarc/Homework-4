result=[]
while True:
    line=input()
    if line=='-1':
        break
    fname=line.split(' ')[0]
    try:
        age=int(line.split(' ')[1])
    except:
        age=0
    result.append([fname,age])

for i in result:
    if i[1]!=0:
        print(f'{i[0]} {(i[1]+1)}')
    else:
        print(f'{i[0]} {i[1]}')
