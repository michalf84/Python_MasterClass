from pyspark.sql import *
from pyspark.sql.functions import spark_partition_id

from lib.logger import Log4j



if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("SparkSchemaDemo") \
        .getOrCreate()

    logger = Log4j(spark)

    flightTimeParquetDF = spark.read \
        .format("parquet") \
        .load("dataSource/flight*.parquet")

    logger.info("Num Partitions before: " + str(flightTimeParquetDF.rdd.getNumPartitions()))
    flightTimeParquetDF.groupBy(spark_partition_id()).count().show()

    flightTimeParquetDF.write \
        .format("csv") \
        .mode("overwrite") \
        .option("path", "dataSink/csv/") \
        .partitionBy("OP_CARRIER", "ORIGIN") \
        # .option("maxRecordsPerFile", 10000) \
        .save()
