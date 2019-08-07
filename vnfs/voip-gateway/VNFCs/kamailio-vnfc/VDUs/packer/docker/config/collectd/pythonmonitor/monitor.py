import collectd
import os
import socket
import urllib
import urllib2
import json


def configer(ObjConfiguration):
  collectd.info('Configuring Stuff') 

def initer():
  collectd.info('initing stuff')

def get_resource_guid():
  resource_guid = os.popen("getProperty resource_id").read().strip()
  
  collectd.info(resource_guid)
  if resource_guid == "no params file found":
    collectd.info('no params file found')
    return None
  if resource_guid == '':
    collectd.info('no resource_guid found')
    return None
  return resource_guid

def isActive():
  path = '/tmp/lifecycle_state'
  if not os.path.exists(path):
      return False
  with open(path, 'r') as lifecycle_state:
    state=lifecycle_state.read().strip()
    collectd.info(state)
    if state=='ACTIVE':
        return True
    return False  
    
def dispatch_metric(plugin, metric, value):
  metric = collectd.Values()
  metric.plugin = plugin
  metric.plugin_instance = get_resource_guid()
  metric.host = socket.gethostname()
  metric.interval = 5
  metric.type = 'gauge'
  metric.type_instance = metric
  metric.values = [value]
  metric.dispatch()
    
  
def send_integrity_metric():
  collectd.info('send_integrity_metric')
	
  resource_guid = get_resource_guid()
  if resource_guid == None:
	return

  state = 'OK'
  pid = os.popen("pgrep asterisk").read()
  if pid == '':
	collectd.info('asterisk not running')
	state = 'BROKEN'
	
  url = 'http://mgmt:8285/api/send/integrity/' + resource_guid + '?metricName=h_integrity&integrity=' + state
  collectd.info(url) 
  try:  urllib2.urlopen(url)
  except Exception as e:
    collectd.info('Send metric request failed')

def send_heal_request():
  collectd.info('send_heal_request')
  resource_guid = get_resource_guid()
  if resource_guid == None:
	return
	
  delim = "__"	
  hostname = socket.gethostname() 
  if hostname.find(delim) == -1:
	collectd.info('unexpected hostname format, cannot extract top level assembly external id')
	return
  external_id = hostname.split(delim)[0]
  collectd.info('external_id ' + external_id)
  
  url = "http://mgmt:8281/api/orchestrator/events"
  body = '{"externalId":"' + external_id + '","eventName":"Heal","properties":{"componentId":"' + resource_guid +'"}}'
  collectd.info(body)
  
  req = urllib2.Request(url)
  req.add_header('Content-Type', 'application/json')
  try: urllib2.urlopen(req, body)
  except Exception as e:
    collectd.info('Heal request failed')

def dispatch_metric(plugin, metric_name, value):
  metric = collectd.Values()
  metric.plugin = plugin
  metric.plugin_instance = get_resource_guid()
  metric.host = socket.gethostname()
  metric.interval = 5
  metric.type = 'gauge'
  metric.type_instance = metric_name
  metric.values = [value]
  metric.dispatch()
    
def dispatch_service_metrics(): 
  raw = os.popen('asterisk -rx "core show calls uptime"').read()
  # expect first line
  # 10 active calls 
  lines = raw.splitlines()
  if len(lines) < 1:
    return    
  active_calls = int(lines[0].split()[0])
  dispatch_metric('asterisk', 'active_calls', active_calls) 
  
  
def read_callback(data=None):
  collectd.info('reading value')
  
  if isActive():
    send_integrity_metric()
    
  dispatch_service_metrics()
  

collectd.register_config(configer)
collectd.register_init(initer)
collectd.register_read(read_callback)
