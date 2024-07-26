#! /bin/bash

hdfs dfs -mkdir /kafka_demo
hdfs dfs -touchz /kafka_demo/tweets_data.json
hdfs dfs -cat /kafka_demo/tweets_data.json
