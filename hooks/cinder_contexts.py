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
        ctxt = []
        missing = []
        for k in self._config_keys:
            if config(k):
                ctxt.append(("{}".format(k.replace('-', '_')),
                             config(k)))
            else:
                missing.append(k)
        if missing:
            raise PureIncompleteConfiguration(
                'Missing configuration: {}.'.format(missing)
            )

        service = service_name()
        ctxt.append(('volume_backend_name', service))
        volume_driver = 'cinder.volume.drivers.pure.PureISCSIDriver'
        ctxt.append(('volume_driver', volume_driver))
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
