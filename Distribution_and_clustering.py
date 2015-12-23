__author__ = 'rocky'
# date_pool=['20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
#date_pool=['20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327'];
date_pool=['20121111','20121114']
grad_size=50
for date in date_pool:
    print date
    DATE=date
    date=date+'Child'
    file=open(date+'.csv')
    File=open(date+'DIST.csv','wt')
    file2=open(date+'Clusters.csv','wt')
    file3=open(date+'ClusterCenter.csv','wt')
    file4=open(date+'ClusterDensity.csv','wt')
    dence={}
    dencity_cluster=[0,0,0,0,0,0,0,0,0,0]
    for x in range(-860,1000):
        dence[x]={}
        for y in range(-620,525):
            dence[x][y]=0
    print 'dense matrix initiated'
    while 1:
        line=file.readline()
        if line =='':
            break
        line=line.strip().split(',')
        x=int(float(line[0])/grad_size)
        y=int(float(line[1])/grad_size)
        if x<1000 and x>-861 and y<525 and y>-621:

            dence[x][y]=dence[x][y]+1
    print 'dense matrix done'
    for y in range(-620,525):
        a=''
        for x in range(-860,1000):
            a=a+str(dence[x][y])+', '
        a=a.rstrip(', ')
        File.write(a+'\n')
    File.close()
    file.close()
    file=open(DATE+"cluster.csv")
    data_array=str(file.readlines())
    data_array=filter(lambda ch: ch in '0123456789.,e-+', data_array)
    data_array=data_array.split(',')

    clusterCenter = [int(float(x) / grad_size) for x in data_array]
    print 'cluster center get'

    for y in range(-620,525):
        a=''
        for x in range(-860,1000):
            i=1
            min_dist=10000000000000000
            while i<len(clusterCenter):
                d=(float(clusterCenter[i-1])-x)**2+(float(clusterCenter[i]-y))**2
                if d<min_dist:
                    min_dist=d
                    color=i
                i+=2
            dencity_cluster[(color-1)/2]=dencity_cluster[(color-1)/2]+dence[x][y]
            if  (y>521 or y<-616 or x>996 or x<-856):
                color=0
            elif dence[x][y]==0 and not ((dence[x-3][y] and dence[x+3][y]) or (dence[x][y-3] and dence[x][y+3])):
                color=0
            a=a+str(color)+', '
        a=a.rstrip(', ')
        file2.write(a+'\n')
    i=1
    print 'cluster mark done'
    while i<len(clusterCenter):
        file3.write(str(float(clusterCenter[i-1])+840)+', '+str(float(clusterCenter[i])+580)+'\n')
        i+=2

    file.close()
    File.close()
    file2.close()
    file3.close()
    file2=open(date+'Clusters.csv')
    print 'Generate cluster density'
    while 1:
        line=file2.readline()
        if line =='':
            break
        line=line.strip().split(', ')
        a=''
        for i in line:
            if int(i)==0:
                a=a+'0, '
            else:
                a=a+str(dencity_cluster[(int(i)-1)/2])+', '
        a=a.rstrip(', ')
        file4.write(a+'\n')
    print 'cluster popolarity done'
    file2.close()
    file4.close()
# file=open('20121024.csv')
# File=open('20121024aizhuozhuo.csv','wt')
# dence={}
# while 1:
#     line=file.readline()
#     if line =='':
#         break
#     line=line.strip().split(',')
#     x=int(float(line[0])/50)
#     y=int(float(line[1])/50)
#     if x in dence.keys():
#         if y in dence[x].keys():
#             dence[x][y]=dence[x][y]+1
#         else:
#             dence[x][y]=1
#     else:
#         dence[x] = {}
#         dence[x][y] = 1
# for x in dence.keys():
#     for y in dence[x].keys():
#         File.write(str(x)+', '+str(y)+','+str(dence[x][y])+'\n')
#
# file.close()
# File.close()