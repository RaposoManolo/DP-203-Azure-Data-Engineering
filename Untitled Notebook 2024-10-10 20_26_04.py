# Databricks notebook source
spark.conf.set(
    "fs.azure.account.key.imrdatalakedev.dfs.core.windows.net","secretKEY")

# COMMAND ----------

df= spark.read.format("csv").load("abfss://bronze@imrdatalakedev.dfs.core.windows.net/Project 1 - Dividends/CashStatements_07102024.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta").save("abfss://silver@imrdatalakedev.dfs.core.windows.net/Dividends_01092024")