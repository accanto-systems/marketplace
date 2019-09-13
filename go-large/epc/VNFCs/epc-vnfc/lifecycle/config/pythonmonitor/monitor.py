import collectd
import os
import socket
import yaml
import urllib
import urllib2
import json
import subprocess

dispatchList=None
last2xx=0

max=15.0

hostname= "{{hostname}}"

def configer(ObjConfiguration):
  collectd.info('Configuring Stuff')

def initer():
  collectd.info('initing stuff')

def readDispatchList():
  global dispatchList
  if os.path.exists('/usr/local/etc/kamailio/dispatcher.list'):
    with open('/usr/local/etc/kamailio/dispatcher.list', 'rt') as f:
      dispatchList = yaml.safe_load(f.read())
  else:
    print ('no dispatch list found')

def get_resource_guid():
  resource_guid = "{{instanceid}}"
  collectd.info(resource_guid)
  return resource_guid

def send_load_metric(load):
  collectd.info('send_load_metric: ' + str(load))

  resource_guid = get_resource_guid()
  if resource_guid == None:
    return

  query_args = { 'metricName':'h_load', 'load':load }
  encoded_args = urllib.urlencode(query_args)

  url = 'http://{{relay_endpoint}}/api/send/load/'+resource_guid+'/?'+encoded_args
  collectd.info(url)

  collectd.info( urllib2.urlopen(url).read())
  dispatch_service_metrics(load, "Load")


# jjh: I re-wrote this function because kamailio frequently has spike in the current:
# It's something going on between kamailio and asterisk, because the 4xx number increases
# but 2xx and is refelecting any current SIPP calls.
# Soooo...for now, basing transactions off 2xx. This refelects the inbound traffic much better
def get_current_transactions():
  global last2xx
  result = subprocess.check_output(['kamcmd', 'tm.stats'])
  collectd.info('tm.stats: ' + result)
  collectd.info('last2xx: ' + str(last2xx))
  resultlist=result.split()
  transactions = 0
  if '2xx:' in resultlist:
    currentIndex=resultlist.index('2xx:')
    current2xx = int(resultlist[currentIndex+1])
    collectd.info('current 2xx: '  + str(current2xx))
    transactions = current2xx - last2xx
    last2xx = current2xx
  collectd.info('transactions: ' + str(transactions))
  return transactions


def dispatch_service_metrics(value, metricName):
  collectd.info('metric: ' + metricName + " value:" + str(value))
  metric = collectd.Values()
  metric.plugin = 'kamailio'
  metric.plugin_instance = get_resource_guid()
  metric.host = hostname
  metric.interval = 5
  metric.type = 'gauge'
  metric.type_instance = metricName
  metric.values = [value]
  metric.dispatch()

def servers_in_dispatchList():
  global dispatchList
  readDispatchList()
  num = sum(1 for line in open('/usr/local/etc/kamailio/dispatcher.list'))
  if 'list' in dispatchList:
      # get the number of servers in dispatchers list
      num=len(dispatchList['list'])
      collectd.info('number of servers in dispatchList: ' + str(num))
  return num

def transactions_per_server():
  # Assuming this is working as a proxy loadbalancing transactions to the servers in dispatch list
  # So approx half the transactions will be incoming calls and half will outgoing to pool.
  current_transactions=get_current_transactions()/2.0

  servers = servers_in_dispatchList()
  per_server = 0.0
  if servers > 0.0:
        per_server = current_transactions/servers
  collectd.info('approx transactions being dispatched per server: ' + str(per_server))
  
  dispatch_service_metrics(current_transactions, 'current transactions')
  dispatch_service_metrics(servers , 'managed_servers')
  return per_server

def load():
  # load is a given as a percentage
  MAX_TRANSACTION_PER_SERVER = 15.0
  load = (transactions_per_server()/MAX_TRANSACTION_PER_SERVER)* 100.0
  if load > 100.0:
        load = 100
  collectd.info('load: ' + str(load))
  
  return int(load)

def read_callback(data=None):
  collectd.info('reading value')

 

  send_load_metric(load())
  
  #dispatch_service_metrics()


collectd.register_config(configer)
collectd.register_init(initer)
collectd.register_read(read_callback)
