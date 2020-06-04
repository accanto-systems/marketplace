def getOutputs(keg, props, resultBuilder, log, *args, **kwargs):
    found, service = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'], namespace='default')
    if not found:
        return resultBuilder.failed('Could not find sipp Pod')
    resultBuilder.setOutput('podname', props['system_properties']['resource_subdomain'])