from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import collectd
import socket
import os

producer = KafkaProducer(	value_serializer=lambda m: json.dumps(m).encode('ascii'), 
							bootstrap_servers='kafka:9092')

def send_metric( metric_name, value, sender=None, metricKey=None):
  kafka_topic="resource_metrics"
  if sender == None:
    sender = socket.gethostname()
  if metricKey == None:
    metricKey = get_property('metricKey')
  try:
    kafka_metric={'metricKey': metricKey,
				'metric_name': metric_name,
				'value': value,
				'sender': sender}
    producer.send(kafka_topic, kafka_metric)

    producer.flush()
  except Exception as e:
    collectd.info('send_metric to kafka ' + kafka_topic + ' failed')


def get_property(property):
  value = os.popen("getProperty " + property).read().strip()
  
  collectd.info(property +': ' + str(value))
  if value == "no params file found":
    collectd.info('no params file found')
    return None
  if value == '':
    collectd.info(property + ' not found')
    return None
  return value
    