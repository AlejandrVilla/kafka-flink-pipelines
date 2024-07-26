#!/usr/bin/env bash

# DOWNLOAD_URL=https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.15.2/flink-sql-connector-kafka-1.15.2.jar
DOWNLOAD_URL=https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.2.0-1.19/flink-sql-connector-kafka-3.2.0-1.19.jar
JAR_PATH=/usr/lib/flink/lib/flink-sql-connector-kafka-3.2.0.jar
sudo chmod 777 /usr/lib/flink/lib/flink-sql-connector-kafka-3.2.0.jar
sudo curl -L -o ${JAR_PATH} ${DOWNLOAD_URL}


# SCRIPT_DIR="$(cd $(dirname "$0"); pwd)"
# SRC_PATH=$SCRIPT_DIR/package
# rm -rf $SRC_PATH && mkdir -p $SRC_PATH/lib
# ## Download flink sql connector kafka
# echo "download flink sql connector kafka..."
# VERSION=1.15.2
# FILE_NAME=flink-sql-connector-kafka-$VERSION
# DOWNLOAD_URL=https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/$VERSION/flink-sql-connector-kafka-$VERSION.jar
# curl -L -o $SRC_PATH/lib/$FILE_NAME.jar ${DOWNLOAD_URL}

## Install pip packages
# echo "install and zip pip packages..."
# pip install -r requirements.txt --target $SRC_PATH/site_packages

## Package pyflink app
# echo "package pyflink app"
# zip -r kda-package.zip processor.py package/lib package/site_packages