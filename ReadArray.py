__author__ = 'rocky'
file=open("try.csv")

data_array=str(file.readlines())
print data_array
data_array=filter(lambda ch: ch in '0123456789.,e-+', data_array)
data_array=data_array.split(', ')
print data_array
# data_array = [int(float(x) / grad_size) for x in clusterCenter]