def getOutputs(keg, props, resultBuilder, log, *args, **kwargs):
    found, service = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'], namespace='default')
    if not found:
        return resultBuilder.failed('Could not find ippbx Pod')
    resultBuilder.setOutput('voice_ip_address', service['status']['podIP'])
    resultBuilder.setOutput('mgmt_ip_address', service['status']['podIP'])
    resultBuilder.setOutput('podname', props['system_properties']['resource_subdomain'])