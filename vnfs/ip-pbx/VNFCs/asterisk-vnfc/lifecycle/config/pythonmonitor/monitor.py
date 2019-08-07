import collectd
import os
import socket
import urllib
import urllib2
import json

hostname = "{{instance_name}}"

def configer(ObjConfiguration):
  collectd.info('Configuring Stuff') 

def initer():
  collectd.info('initing stuff')

def get_metric_key():
  metric_key = "{{instanceid}}"
  
  collectd.info(metric_key)
  if metric_key == "no params file found":
    collectd.info('no params file found')
    return None
  if metric_key == '':
    collectd.info('no metric_key found')
    return None
  return metric_key


    
def dispatch_metric(plugin, metric_name, value):
  metric = collectd.Values()
  metric.plugin = plugin
  metric.plugin_instance = get_metric_key()
  metric.host = hostname
  metric.interval = 5
  metric.type = 'gauge'
  metric.type_instance = metric_name
  metric.values = [value]
  metric.dispatch()
    
  
def send_integrity_metric():
  collectd.info('send_integrity_metric')
	
  metric_key = get_metric_key()
  if metric_key == None:
	return

  state = 'OK'
  state_int = 1
  pid = os.popen("pgrep asterisk").read()
  if pid == '':
	collectd.info('asterisk not running')
	state = 'BROKEN'
	state_int = 0
	
  url = 'http://{{relay_endpoint}}/api/send/integrity/' + metric_key + '?metricName=h_integrity&integrity=' + state
  collectd.info(url) 
  try:  urllib2.urlopen(url)
  except Exception as e:
    collectd.info('Send metric request failed')
  
  dispatch_metric('asterisk', 'integrity', str(state_int))


    
def dispatch_service_metrics(): 
  raw = os.popen('asterisk -rx "core show calls uptime"').read()
  # expect first line
  # 10 active calls 
  lines = raw.splitlines()
  if len(lines) < 1:
    return    
  active_calls = int(lines[0].split()[0])
  collectd.info('Send service metric request' + str(active_calls))
  dispatch_metric('asterisk', 'active_calls', active_calls) 
  
  
def read_callback(data=None):
  collectd.info('reading value')
  
  
  send_integrity_metric()
    
  dispatch_service_metrics()
  

collectd.register_config(configer)
collectd.register_init(initer)
collectd.register_read(read_callback)

