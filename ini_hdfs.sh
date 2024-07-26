#! /bin/bash

hadoop fs -mkdir /kafka_demo
hadoop fs -touchz /kafka_demo/tweets_data.json
hadoop fs -cat /kafka_demo/tweets_data.json
