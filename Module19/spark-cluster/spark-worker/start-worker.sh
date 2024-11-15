#!/bin/bash

# Wait until the Spark master is available
until curl -s http://spark-master:8080 > /dev/null; do
  echo "Waiting for Spark master to be available..."
  sleep 2
done

# Start the Spark worker node
$SPARK_HOME/sbin/start-worker.sh spark://spark-master:7077

# Keep the container running
tail -f $SPARK_HOME/logs/spark--org.apache.spark.deploy.worker.Worker-*.out
