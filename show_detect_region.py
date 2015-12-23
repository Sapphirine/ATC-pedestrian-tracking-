__author__ = 'rocky'
date='20121028'
file=open(date+'.csv')
File=open('detect_region.csv','wt')
grad_size=50
dence={}
dencity_cluster=[0,0,0,0,0,0,0,0,0,0]
for x in range(-860,1000):
    dence[x]={}
    for y in range(-620,525):
        dence[x][y]=0

while 1:
    line=file.readline()
    if line =='':
        break
    line=line.strip().split(',')
    x=int(float(line[0])/grad_size)
    y=int(float(line[1])/grad_size)
    if x<1000 and x>-861 and y<525 and y>-621:

        dence[x][y]=1
    if x>-460 and x<-60 and y<0:
        dence[x][y]=5
for y in range(-620,525):
    a=''
    for x in range(-860,1000):
        a=a+str(dence[x][y])+', '
    a=a.rstrip(', ')
    File.write(a+'\n')
file.close()
File.close()