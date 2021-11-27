from pyspark.sql import *
from pyspark.sql.functions import spark_partition_id, column, col, expr, to_date, concat

from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("SparkSchemaDemo") \
        .getOrCreate()

    logger = Log4j(spark)


airlineDF=spark.read\
    .format("csv") \
    .option("header","true")\
    .option("inferSchema","true")\
    .option("sampleRation","0.0001") \
    .load("sample.csv")

airlineDF.select("Origin","Dest","Distance").show(10)

airlineDF.select(column("Origin"),col("Dest"),airlineDF.Distance).show(10)


# how to create column expressions
# first option
airlineDF.select( column("Origin"),col("Dest"),airlineDF.Distance,expr("to_date(concat(Year,Month,Day),'yyyyMMdd') as flihtdate")).show(10)
# last option
airlineDF.select( column("Origin"),col("Dest"),airlineDF.Distance,to_date(  concat("Year","Month","Day"),'yyyyMMdd').alias("flihtdate")).show(10)

