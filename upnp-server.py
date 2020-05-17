#!/usr/bin/python3

import upnp


def start_server():
    device = upnp.Device({
        'deviceType': 'urn:schemas-upnp-org:device:MediaServer:1',
        'st': 'urn:schemas-upnp-org:device:MediaServer:1',
        'friendlyName': 'UPnP Test',
        'uuid': '00a56575-78fa-40fe-b107-8f4b5043a2b0',
        'manufacturer': 'Example',
        'manufacturerURL': 'http://example.com',
    })

    for i in range(1, 20):
        service = upnp.Service({
            'serviceType': 'urn:schemas-upnp-org:service:ContentDirectory:1',
            'serviceId': 'example-com:serviceId:%d' % i,
            'controlURL': 'a' * i
        })
        device.addService(service)

    server = upnp.Announcer(device)
    server.initLoop()
    server.notify()
    server.forever()
    server.dispose()


if __name__ == '__main__':
    start_server()
