from charmhelpers.core.hookenv import (
    config,
    service_name
)

from charmhelpers.contrib.openstack.context import (
    OSContextGenerator,
)


class PureIncompleteConfiguration(Exception):
    pass


class PureSubordinateContext(OSContextGenerator):
    interfaces = ['pure-flasharray']

    _config_keys = [
        'san_ip',
        'pure_api_token',
    ]

    def __call__(self):
    
        required_keys = ['protocol', 'san_ip', 'pure_api_token']

        for key in required_keys:
            if not config(k): 
              raise PureIncompleteConfiguration(
                  'Missing configuration setting "%s"' % key)

        ctxt = []
        for k in self._config_keys:
            if config(k):
                ctxt.append(("{}",config(k)))

        protocol = config('protocol').lower()
        if protocol not in drivers.key():
           raise PureIncompleteConfiguration(
               '"%s" is not a valid protocol option' % protocol)
        service = service_name()
        ctxt.append(('volume_backend_name', service))
        drivers = {
            'iscsi': 'cinder.volume.drivers.pure.PureISCSIDriver',
            'fc': 'cinder.volume.drivers.pure.PureFCIDriver',
        }
        ctxt.append(('volume_driver', drivers[protocol]))
        ctxt.append(('use_multipath_for_image_xfer', 'true'))
        return {
            "cinder": {
                "/etc/cinder/cinder.conf": {
                    "sections": {
                        service: ctxt,
                    }
                }
            }
        }
