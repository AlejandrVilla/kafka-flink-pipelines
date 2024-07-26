# Import necessary libraries
from kafka import KafkaConsumer
from json import loads
from rich import print
import pydoop.hdfs as hdfs

# Create a Kafka consumer
consumer = KafkaConsumer(
    'my-topic-test',  # Topic to consume messages from
    bootstrap_servers=['ip-172-31-85-30.ec2.internal:9092'],  # Kafka server addresses
    auto_offset_reset='earliest',  # Reset offset to the earliest available message
    enable_auto_commit=True,  # Enable auto commit of consumed messages
    group_id=None,  # Consumer group ID (None indicates an individual consumer)
    value_deserializer=lambda x: loads(x.decode('utf-8'))  # Deserialize the message value from JSON to Python object
)

# hdfs_path = 'hdfs://VPS-DATA1:9000/kafka_demo/tweets_data.json'
hdfs_path = 'hdfs://ip-172-31-85-30.ec2.internal:8020/kafka_demo/tweets_data.json'  # Path to the HDFS file

# Process incoming messages
for message in consumer:
    tweet = message.value  # Get the value of the message (tweet)
    print(tweet)  # Print the tweet

    with hdfs.open(hdfs_path, 'at') as file:
        print("Storing in HDFS!")
        file.write(f"{tweet}\n")
