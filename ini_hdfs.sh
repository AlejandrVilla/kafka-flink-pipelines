#! /bin/bash

sudo su - hdfs
echo "creando carpetas en hdfs para kafka"
hdfs dfs -mkdir /kafka_hdfs
hdfs dfs -touchz /kafka_hdfs/tweets_data.json
hdfs dfs -ls /kafka_hdf/

echo "creando carpetas en hdfs para flink"
hdfs dfs -mkdir /flink_hdfs
hdfs dfs -touchz /flink_hdfs/tweets_data.json
hdfs dfs -ls /flink_hdfs/
