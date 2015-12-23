__author__ = 'rocky'
date_pool=['20121111']
for date in date_pool:
    file0=open(date+'speedavg.csv')
    file1=open(date+"ClusterSpeedCenter.csv")
    file2=open(date+'SpeedinCluster.csv','wt')
    data_array=str(file1.readlines())
    data_array=filter(lambda ch: ch in '0123456789.,e-+', data_array)
    data_array=data_array.split(',')
    clusterCenter = [int(float(x)) for x in data_array]
    speedCenter=[clusterCenter[0],clusterCenter[2],clusterCenter[4],clusterCenter[6],clusterCenter[8]]
    speedCenter=sorted(speedCenter)
    print speedCenter
    comparator=[(speedCenter[0]+speedCenter[1])/2,(speedCenter[1]+speedCenter[2])/2,(speedCenter[2]+speedCenter[3])/2,(speedCenter[3]+speedCenter[4])/2]
    print comparator
    while 1:
        a=''
        line=file0.readline()
        line=line.strip().rstrip('\n')
        if line=='':
            break
        lines=line.strip().split(',')
        for num in lines:
            if float(num)==0:
                a=a+'0 '
            elif float(num)<comparator[0]:
                a=a+'1 '
            elif float(num)<comparator[1]:
                a=a+'2 '
            elif float(num)<comparator[2]:
                a=a+'3 '
            elif float(num)<comparator[3]:
                a=a+'4 '
            else:
                a=a+'5 '
        a=a.rstrip(' ')
        file2.write(a+'\n')
    file0.close()
    file1.close()
    file2.close()