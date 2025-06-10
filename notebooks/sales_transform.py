# Databricks notebook source
# MAGIC %md
# MAGIC ## Retail Sales Data Transformation

# COMMAND ----------
from pyspark.sql.functions import col, to_date

df = spark.read.csv("/dbfs/FileStore/tables/sales_data.csv", header=True, inferSchema=True)
df_clean = df.withColumn("SaleDate", to_date(col("SaleDate"), "yyyy-MM-dd"))
df_clean.createOrReplaceTempView("sales_clean")
