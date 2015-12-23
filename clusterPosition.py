__author__ = 'rocky'
from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array
from math import sqrt
from pyspark import SparkContext
sc =SparkContext()
#date_pool=['20121028','20121031','20121104','20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327']
date_pool=['20121111']
for date in date_pool:
    print date+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'
    File=open(date+'ClusterSpeedCenter.csv','wt')
    # Load and parse the data
    data = sc.textFile(str(date)+'ClusterSpeed.csv')
    rdd = data.map(lambda line: array([float(x) for x in line.split(',')]))
    clusters = KMeans.train(rdd, 5, maxIterations=10, runs=10, initializationMode="random")
    File.write(str(clusters.centers))
    File.close()
# test = clusters.predict(rdd)
# clusters.save(sc, "myModelPath")
# test.save("test")

# print "dataIS"
# print data
# #rdd = sc.textFile("test.csv").map(lambda (name,text):text.split(','))
#
# #print "parsedData"
# #print parsedData
# # Build the model (cluster the data)
# clusters = KMeans.train(rdd, 2, maxIterations=10, runs=10, initializationMode="random")
# #clusters = model.predict(rdd)
# test = clusters.predict(rdd)
# #dataWithClusters = rdd.zip(clusters)
# clusters.save(sc, "myModelPath")
# test.save("test")
# #dataWithClusters.saveAsTextFile()
# #print "clusters"
# #print clusters
# # Evaluate clustering by computing Within Set Sum of Squared Errors
# # def error(point):
# #     center = clusters.centers[clusters.predict(point)]
# #     return sqrt(sum([x**2 for x in (point - center)]))
# #
# # WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
# # print("Within Set Sum of Squared Error = " + str(WSSSE))
# #
# # # Save and load model
# # clusters.save(sc, "myModelPath")
# # sameModel = KMeansModel.load(sc, "myModelPath")