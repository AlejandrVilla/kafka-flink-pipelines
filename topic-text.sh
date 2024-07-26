#! /bin/bash

cd ~/kafka-3.4/
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic test-topic
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list