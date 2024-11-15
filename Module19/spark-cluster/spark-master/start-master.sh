#!/bin/bash

# Start the Spark master node
$SPARK_HOME/sbin/start-master.sh

# Keep the container running
tail -f $SPARK_HOME/logs/spark--org.apache.spark.deploy.master.Master-*.out
