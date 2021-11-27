import configparser

from pyspark import SparkConf


def load_survey(spark,filename):
    return spark.read \
        .option("header","true") \
        .option("inferSchema","true") \
        .csv(filename)     # variable file name


def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key, val)
    return spark_conf


def count_by_country(dataframe):
    return dataframe \
        .where("Age<40").select("Age","Gender","Country","state").groupBy("Country").count()
