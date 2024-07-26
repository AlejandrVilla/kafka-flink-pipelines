#! /bin/bash

cd ~/kafka-3.4/
bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092
