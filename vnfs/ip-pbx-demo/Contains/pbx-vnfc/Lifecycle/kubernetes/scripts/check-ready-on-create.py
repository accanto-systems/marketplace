def checkReady(keg, props, resultBuilder, log, *args, **kwargs):
    found, pod = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'], namespace='default')
    if not found:
        return resultBuilder.failed(f'Could not find ippbx Pod')
    # found2, pod2 = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'] + "-2", namespace='default')
    # if not found2:
    #     return resultBuilder.failed(f'Could not find ippbx Pod 2')
    # found3, pod3 = keg.objects.get('v1', 'Pod', props['system_properties']['resource_subdomain'] + "-3", namespace='default')
    # if not found3:
    #     return resultBuilder.failed(f'Could not find ippbx Pod 3')

    if pod['status']['phase'] == 'Running':
        return resultBuilder.ready()
    else:
        return resultBuilder.notReady()

