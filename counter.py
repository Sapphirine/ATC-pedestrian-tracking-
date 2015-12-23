# __author__ = 'rocky'
# date_pool=['20121024','20121028','20121031','20121104','20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
date_pool=['atc20121111_child_sort', 'atc20121114_child_sort']
for date in date_pool:
    print date
    # file=open('atc-'+date+'.csv')
    file=open(date+'.txt')

    File=open(date+'Child.csv','wt')
    while 1:
        line=file.readline()
        if line=='':
            break
        lines=line.strip().split('\t')
        lines=lines[2]+','+lines[3]+'\n'

        File.write(lines)
    file.close()
    File.close()

# file=open('atc-20121024.csv')
# File=open('try.csv','wt')
# while 1:
#     try:
#         line=file.readline()
#     except:
#         break
#     lines=line.strip().split(',')
#     if lines[4]>1200:
#         lines=lines[0]+','+lines[1]+','+lines[2]+','+lines[3]+','+lines[4]+','+lines[5]+','+lines[6]+','+lines[7]+','+'1'+'\n'
#     else:
#         lines=lines[0]+','+lines[1]+','+lines[2]+','+lines[3]+','+lines[4]+','+lines[5]+','+lines[6]+','+lines[7]+','+'0'+'\n'
#
#     File.write(lines)
# file.close()
# File.close()
