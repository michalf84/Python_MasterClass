import sys
from pyspark.sql import *
from lib.logger import Log4j
from lib.untils_mich import *

if __name__ == "__main__":
    conf = get_spark_app_config()

    spark = SparkSession \
        .builder \
        .config(conf=conf) \
        .getOrCreate()

    logger = Log4j(spark)

    if len(sys.argv) != 2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)
    logger.info("Starting HelloSpark")

    survey_df=load_survey(spark,sys.argv[1])
    paritioned_survey_df=survey_df.repartition(2)

    count_df=count_by_country(paritioned_survey_df)

    logger.info(count_df.collect())

    input("Press Enter")
    logger.info("Finished HelloSpark")
    spark.stop()
