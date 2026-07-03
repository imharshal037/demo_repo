import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\Harshal\AppData\Local\Programs\Python\Python314\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\Harshal\AppData\Local\Programs\Python\Python314\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("pysparkobj")\
        .getOrCreate()

print(spark.version)

# data = [
#     (1, "Alice", 50000),]

# df = spark.createDataFrame(data, ["id", "name", "salary"])

df = spark.read.option("header", "true").option("inferSchema", "true").csv(r"D:/Harshal Patil/Project/Python/data.csv") 

df.show()

print("Number of partitions:", df.rdd.getNumPartitions())


