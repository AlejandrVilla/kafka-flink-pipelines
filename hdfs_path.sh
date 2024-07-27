#! /bin/bash

# cat /etc/hadoop/conf/core-site.xml | grep dfs
hdfs getconf -confKey fs.defaultFS
