#! /bin/bash

cd kafka-3.4/kafka_2.12-3.4.0
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic anishmahapatra
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list