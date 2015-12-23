__author__ = 'rocky'
file=open('pigFortime1.csv')
File=open('stayTime.csv','wt')
origin='hehe'
t=0
while 1:
    try:
        line=file.readline()
    except:
        pass
    #     print 'hehe'
    #     break
    print line
    line=line.strip().split()
    if line[1]==origin:
        t=float(line[0])-start
    else:
        File.write(origin+', '+str(t))
        origin=line[1]
        start=line[0]
    file.close()
    File.close()

