__author__ = 'rocky'
__author__ = 'rocky'
# date_pool=['20121024','20121028','20121031','20121104','20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
date_pool=['20121111']
grad_size=50
pi=3.1415926
jud_ang=pi/2
for date in date_pool:
    print date
    # file=open('atc-'+date+'.csv')
    file=open('atc-'+date+'.csv')
    File=open(date+'speedavg.csv','wt')

    # line=file.readline()
    # line=line.strip().split(',')
    # time0=float(line[0])

    dence_walk={}
    dence_walk_count={}
    speedAvg={}
    for x in range(-860,1000):
        dence_walk[x]={}
        dence_walk_count[x]={}
        speedAvg[x]={}
        for y in range(-620,525):
            dence_walk[x][y]=0
            dence_walk_count[x][y]=0
            speedAvg[x][y]=0

    print 'dense matrix initiated'
    while 1:
        line=file.readline()
        if line =='':
            break
        line=line.strip().split(',')
        speed=float(line[5])
        x=int(float(line[2])/grad_size)
        y=int(float(line[3])/grad_size)
        if x<1000 and x>-861 and y<525 and y>-621:
            dence_walk_count[x][y]=dence_walk_count[x][y]+1
            dence_walk[x][y]=dence_walk[x][y]+speed
    for x in range(-860,1000):
        for y in range(-620,525):
            if dence_walk_count[x][y]!=0:
                speedAvg[x][y]=dence_walk[x][y]/dence_walk_count[x][y]
    for y in range(-620,525):
        write_speed=''
        for x in range(-860,1000):
            write_speed=write_speed+str(speedAvg[x][y])+', '
        write_speed=write_speed.rstrip(', ')
        File.write(write_speed+'\n')
    File.close()