from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder \
    .appName("SparkOptimizationDemo") \
    .getOrCreate()

# Large transaction dataset
transactions = spark.read.parquet("transactions.parquet")

# Small customer dimension dataset
customers = spark.read.parquet("customers.parquet")

# Inefficient join
regular_join = transactions.join(customers, "customer_id")

# Optimized broadcast join
optimized_join = transactions.join(
    broadcast(customers),
    "customer_id"
)

# Sample aggregation
result = optimized_join.groupBy("customer_id").sum("amount")

result.show()

spark.stop()



# Broadcast join reduces shuffle operations
# Useful when joining large dataset with small dimension table
