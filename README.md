## Before create the EMR cluster

- Use the content of pydoop.sh at the beginning of the cration emr cluster [pydoop in emr](https://crs4.github.io/pydoop/installation.html#emr)


## After cluster creation
- Clone the repo
```
sudo yum update -y
sudo yum install git -y
git --version
git clone git@github.com:AlejandrVilla/kafka-flink-pipelines.git
```
- Use ini.sh to get kafka
```
./ini.sh
```

- Set permissions
```
cd kafka-flink-pipelines
sudo chmod u+x *.sh
```

- Install dependencies
```
pip install --ignore-installed -r requirements.txt
```

- Open a shell and start a broker
```
./kafka-server.sh
```

- Open a shell and run standalone server
```
./standalone-server.sh
```

- To crate a topic use
```
./topic-text.sh
```

- To test a producer and a consumer run in separated shels
```
./consumer-test.sh
./producer-test.sh
```
- Then you can add some text to the producer and the consumer must show it

## Set up python producer and consumer
- Change bootstrap_servers in producer and consumer python files (change the ip address)
```
bootstrap_servers=['ip-172-31-85-30.ec2.internal:9092'],  # Kafka server addresses
```

- Run python producer
```
cd twitterKafka/
python kafka_tweets_producer.py
```

- Run python consumer
```
cd twitterKafka/
python kafka_tweets_consumer.py
```


## Set up hdfs
- Change bootstrap_servers in the hdfs consumer python file (change the ip address)
```
bootstrap_servers=['ip-172-31-85-30.ec2.internal:9092'],  # Kafka server addresses
```
 
- Change the hdfs path in hdfs consumer python file (change the ip address)
```
hdfs_path = 'hdfs://ip-172-31-85-30.ec2.internal:8020/kafka_demo/tweets_data.json'  
```

- Run hdfs consumer
```
cd twitterKafka/
python hdfs_consumer.py
```

## Set up flink
- Use kaf-conector.sh to add flink-sql-connector-kafka-1.15.2.jar to flink configuration and link kafka and flink
```
./kafka-conector.sh
```

- Run flink streaming
```
cd realTimeStreaming/"kafkaFlinkPipeline"
python kafka_flink_streaming.py
```

## other
```
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/include/
```


