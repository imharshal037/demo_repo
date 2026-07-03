import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\Harshal\AppData\Local\Programs\Python\Python314\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\Harshal\AppData\Local\Programs\Python\Python314\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySparkOBJ") \
    .getOrCreate()

import os

print("CPU Core : ",os.cpu_count())

# Sample data
data = [
    (1, "Alice", 50000),
    (2, "Bob", 65000),
    (3, "Charlie", 45000),
    (4, "David", 70000)
]

columns = ["id", "name", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()