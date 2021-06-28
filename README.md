# NOTICE

# THIS CHARM IS SUPERCEEDED BY THE OFFICIAL OPENSTACK CHARM MAINTAINED BY CANONICAL

The source code for this is located at https://opendev.org/openstack/charm-cinder-purestorage

# All details below are no longer relevent and are kept for historical purposes only!!

# Pure Storage FlashArray Storage Backend for Cinder

This charm provides a Pure Storage FlashArray storage backend for use with the Cinder
charm.

## Configuration

The cinder-pure charm requires configuration to allow the driver to access
the Pure Storage FlashArray:

    cinder-pure:
       san_ip: fqdn.array.or.ip
       pure_api_token: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
       protocol: iscsi

Add this configuration in the config.yaml file before deploying the charm.

## Usage

    juju deploy cinder
    juju deploy cinder-pure
    juju add-relation cinder-pure cinder

## Contact Information

Simon Dodsley <simon@purestorage.com>

**As a community project, no warranties are provided for the use of this code.**

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
