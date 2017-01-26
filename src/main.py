from api import Api
import sys


def get_products():
    """Get products from iSales"""
    payload = {'username': '1c_server_tdshkurenk',
               'password': '26208',
               'dtFrom': '20170123',
               'dtTo': '20170126'}

    headers = {'User-Agent': '1C Soap toolkit',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': 'http://tempuri.org/ & ProductsTransfer',
               'Accept-Encoding': 'gzip, deflate'}

    result = API.execute_get_query('/isales/ws/accountingtransfer.asmx/ProductsTransfer', payload, headers)

    if result == None:
        sys.exit(0)
    elif result.status_code != 200:
        sys.exit(0)
    else:
        with open('products.xml', 'w', encoding='utf-8') as f:
            f.write(result.text)

        sys.exit(1)

API = None

API = Api('https://www.isales.pepsico.com', '1c_server_tdshkurenk', '26208')

get_products()
