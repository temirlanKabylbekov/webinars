import zeep


WSDL = 'http://www.soapclient.com/xml/soapresponder.wsdl'


if __name__ == '__main__':
    client = zeep.Client(wsdl=WSDL)
    print(client.service.Method1('Zeep', 'is cool'))
