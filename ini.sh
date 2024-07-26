#! /bin/bash

python3 --version
pip --version
java -version
# scala -version
git --version

# scala
# curl -fL https://github.com/coursier/coursier/releases/latest/download/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup

# kafka
# pushd .
cd ~
wget https://archive.apache.org/dist/kafka/3.4.0/kafka_2.12-3.4.0.tgz
tar -xzf kafka_2.12-3.4.0.tgz
mv kafka_2.12-3.4.0 kafka-3.4
# popd

# cd /path/to/your/flink/directory
# ./bin/jobmanager.sh list