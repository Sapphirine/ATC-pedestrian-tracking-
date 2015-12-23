or__ = 'anitalu'
file1=open('groups_ATC-2.dat')
file2=open('person_ATC-2_1900.csv')
file3=open('group_try_2.csv','a')
group = []

while 1:
    line=file1.readline()
    if line != '':
        line=line.strip().split(' ')
        group.append(line[0])
    else:
        break

while 1:
    line=file2.readline()
    if line != '':
        line=line.strip().split(',')
        if float(line[2]) >= -1 and float(line[2]) <= 9999 and float(line[3]) >= -1 and float(line[3]) <= 9999:
            if line[1] in group:
                line.append('1')
                line = ','.join(line)
                file3.write(line+'\n')
            else:
                line.append('0')
                line = ','.join(line)
                file3.write(line+'\n')
    else:
        break