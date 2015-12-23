__author__ = 'rocky'
# date_pool=['20121024','20121028','20121031','20121104','20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
date_pool=['20130106']
grad_size=50
pi=3.1415926
jud_ang=pi/2
for date in date_pool:
    print date
    # file=open('atc-'+date+'.csv')
    file=open('atc-'+date+'.csv')
    file2=open(date+'SpeedDist.csv','wt')
    file3=open(date+'SpeedDistCount.csv','wt')
    file4=open(date+'StandAng.csv','wt')
    file5=open(date+'StandAngCount.csv','wt')
    #
    # line=file.readline()
    # line=line.strip().split(',')
    # time0=float(line[0])

    dence_walk={}
    dence_walk_count={}
    dence_stand={}
    dence_stand_count={}
    dencity_cluster=[0,0,0,0,0,0,0,0,0,0]
    for x in range(-860,1000):
        dence_walk[x]={}
        dence_walk_count[x]={}
        dence_stand[x]={}
        dence_stand_count[x]={}
        for y in range(-620,525):
            dence_walk[x][y]=0
            dence_walk_count[x][y]=0
            dence_stand[x][y]=0
            dence_stand_count[x][y]=0

    print 'dense matrix initiated'
    while 1:
        line=file.readline()
        if line =='':
            break
        line=line.strip().split(',')
        time=float(line[0])
        speed=float(line[5])
        if speed>500:
            Motion_Angle=float(line[6])
            x=int(float(line[2])/grad_size)
            y=int(float(line[3])/grad_size)
            if x<1000 and x>-861 and y<525 and y>-621:
                dence_walk_count[x][y]=dence_walk_count[x][y]+1
                dence_walk[x][y]=dence_walk[x][y]+Motion_Angle
        elif speed<200:
            Stand_Angle=float(line[7])
            x=int(float(line[2])/grad_size)
            y=int(float(line[3])/grad_size)
            if x<1000 and x>-861 and y<525 and y>-621:
                dence_stand_count[x][y]=dence_stand_count[x][y]+1
                dence_stand[x][y]=dence_stand[x][y]+Stand_Angle

    print 'dense walk matrix done'
    for y in range(-620,525):
        walk=''
        walk_count=''
        stand=''
        stand_count=''
        for x in range(-860,1000):
            walk=walk+str(dence_walk[x][y])+', '
            walk_count=walk_count+str(dence_walk_count[x][y])+', '
            stand=stand+str(dence_stand[x][y])+', '
            stand_count=stand_count+str(dence_stand_count[x][y])+', '
        walk=walk.rstrip(', ')
        walk_count=walk_count.rstrip(', ')
        stand=stand.rstrip(', ')
        stand_count=stand_count.rstrip(', ')
        file2.write(walk+'\n')
        file3.write(walk_count+'\n')
        file4.write(stand+'\n')
        file5.write(stand_count+'\n')
    file.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file2=open(date+'SpeedDist.csv')
    file3=open(date+'SpeedDistCount.csv')
    file6=open(date+'SpeedAvgAngle.csv','wt')
    file7=open(date+'StandAvgAngle.csv','wt')
    stand_avg_angle={}
    speed_avg_angle={}
    for x in range(-860,1000):
        speed_avg_angle[x]={}
        stand_avg_angle[x]={}
        for y in range(-620,525):
            if dence_walk_count[x][y]!=0:
                avg_angle=dence_walk[x][y]/dence_walk_count[x][y]
                if avg_angle>=pi*3/4 or avg_angle<-pi*3/4:
                    speed_avg_angle[x][y]=4
                elif avg_angle>=pi/4 and avg_angle<pi*3/4:
                    speed_avg_angle[x][y]=3
                elif avg_angle>=-pi*3/4 and avg_angle<-pi/4:
                    speed_avg_angle[x][y]=2
                else:
                    speed_avg_angle[x][y]=1
            else:
                speed_avg_angle[x][y]=0
        for y in range(-620,525):
            if dence_stand_count[x][y]!=0:
                avg_angle=dence_stand[x][y]/dence_stand_count[x][y]
                if avg_angle>=pi*3/4 or avg_angle<-pi*3/4:
                    stand_avg_angle[x][y]=4
                elif avg_angle>=pi/4 and avg_angle<pi*3/4:
                    stand_avg_angle[x][y]=3
                elif avg_angle>=-pi*3/4 and avg_angle<-pi/4:
                    stand_avg_angle[x][y]=2
                else:
                    stand_avg_angle[x][y]=1
            else:
                stand_avg_angle[x][y]=0


    for y in range(-620,525):
        write_avg_angle=''
        write_stand_avg=''
        for x in range(-860,1000):
            write_avg_angle=write_avg_angle+str(speed_avg_angle[x][y])+', '
            write_stand_avg=write_stand_avg+str(stand_avg_angle[x][y])+', '
        write_avg_angle=write_avg_angle.rstrip(', ')
        write_stand_avg=write_stand_avg.rstrip(', ')
        file7.write(write_stand_avg+'\n')
        file6.write(write_avg_angle+'\n')
    file6.close()
    file7.close()