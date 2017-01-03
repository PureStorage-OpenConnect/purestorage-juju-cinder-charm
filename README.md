# Pure Storage FlashArray Storage Backend for Cinder

This charm provides a Pure Storage FlashArray storage backend for use with the Cinder
charm.

## Configuration

The cinder-pure charm has the following mandatory configuration.

1. To access the FlashArray array:
 - san_ip
 - pure_api_token

Add this configuration in the config.yaml file before deploying the charm.

## Usage

    juju deploy cinder
    juju deploy cinder-pure
    juju add-relation cinder-pure cinder

# Contact Information

Simon Dodsley <simon@purestorage.com>
