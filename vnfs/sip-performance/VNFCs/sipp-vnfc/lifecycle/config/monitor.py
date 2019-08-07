import collectd
import os

statsFile=None
hostname="{{ hostname }}"

def configer(ObjConfiguration):
  collectd.info('Configuring Stuff') 

def initer():
  collectd.info('initing stuff')

def read_callback(data=None):

  global statsFile

  if statsFile==None:
    collectd.info('waiting for csv file to appear')

    # check if csv file exists
    for file in os.listdir("/opt/"):
      if file.endswith(".csv"):
        statsFile = open("/opt/"+file, 'r')
        collectd.info('opening file')
        line = statsFile.readline()
        collectd.info(line)

  else:
    collectd.info('reading latest stats from csv')

    where = statsFile.tell()
    line = statsFile.readline()
    if not line:
      statsFile.seek(where)
    else:
      dispatchStats(line)

def dispatchMetric(params, name, position):
  global hostname
  collectd.info('dispatching metric:' + name)
  metric = collectd.Values()
  metric.plugin = 'sipp values'
  metric.host = hostname
  metric.type = 'gauge'
  metric.interval = 5
  metric.type_instance=name
  metric.values = [float(params[position])]
  collectd.info('dispatching metric:' + name + " values:"+str(metric.values))
  metric.dispatch()
  

def dispatchStats(line):
  # parse csv line and convert to collectd metrics
  collectd.info('dispatching stats:' + line)
  params=line.split(';')

  dispatchMetric(params, 'call rate', 7)
  dispatchMetric(params, 'outgoing calls', 11)
  dispatchMetric(params, 'total calls created', 12)
  dispatchMetric(params, 'total successful calls', 15)
  dispatchMetric(params, 'successful calls', 14)
  dispatchMetric(params, 'failed calls', 16)
  dispatchMetric(params, 'total failed calls', 17)
  dispatchMetric(params, 'current calls', 13)

collectd.register_config(configer)
collectd.register_init(initer)
collectd.register_read(read_callback)

