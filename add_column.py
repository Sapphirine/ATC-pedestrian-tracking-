__author__ = 'rocky'
pi=3.1415926
date_pool=['20121028','20121031']
for date in date_pool:
    file=open('atc-'+date+'.csv')
    File=open(date+'addDirectionCol.csv','wt')
    line=file.readline()
    line=line.strip().rstrip('\n')
    lines=line.strip().split(',')
    time0=float(lines[0])
    File.write(line+',0\n')
    while 1:
        line=file.readline()
        line=line.strip().rstrip('\n')
        if line=='':
            break
        lines=line.strip().split(',')
        walk_angle=float(lines[6])
        if walk_angle>=0:
            ns='1'
        else:
            ns='0'
        if walk_angle>=pi/2 or walk_angle<-pi/2:
            we='0'
        else:
            we='1'
        File.write(line+','+ns+','+we+'\n')
    file.close()
    File.close()