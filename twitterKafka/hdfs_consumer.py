# Import necessary libraries
from kafka import KafkaConsumer
from json import loads
from rich import print
import os
import subprocess

# Create a Kafka consumer
consumer = KafkaConsumer(
    'my-topic-test',  # Topic to consume messages from
    bootstrap_servers=['ec2-34-226-148-69.compute-1.amazonaws.com:9092'],  # Kafka server addresses
    auto_offset_reset='earliest',  # Reset offset to the earliest available message
    enable_auto_commit=True,  # Enable auto commit of consumed messages
    group_id=None,  # Consumer group ID (None indicates an individual consumer)
    value_deserializer=lambda x: loads(x.decode('utf-8'))  # Deserialize the message value from JSON to Python object
)

# Local path to store the data temporarily
local_path = '/tmp/tweets_data2.json'

# Ensure the local path exists
os.makedirs(os.path.dirname(local_path), exist_ok=True)

# HDFS path
hdfs_path = '/kafka_demo/tweets_data.json'

# User that will own the file in HDFS
hdfs_user = 'hdfs'  # Change to the appropriate HDFS user

# Process incoming messages
for message in consumer:
    tweet = message.value  # Get the value of the message (tweet)
    print(tweet)  # Print the tweet

    # Write the tweet to the local file
    with open(local_path, 'a', encoding='utf-8') as file:
        print("Storing locally!")
        file.write(f"{tweet}\n")
    
    # Move the local file to HDFS
    subprocess.run(['hdfs', 'dfs', '-put', '-f', local_path, hdfs_path], check=True)

    # Change ownership of the file in HDFS to the HDFS user
    subprocess.run(['hdfs', 'dfs', '-chown', hdfs_user, hdfs_path], check=True)

    # Optional: Remove the local file after moving to HDFS
    os.remove(local_path)