def checkReady(keg, props, resultBuilder, log, *args, **kwargs):
    found, deployment = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'], namespace='default')
    if not found:
        return resultBuilder.failed(f'Could not find sipp Pod')
    return resultBuilder.ready()
