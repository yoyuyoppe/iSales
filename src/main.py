from api import Api
import sys
import my_parser


def get_products():
    """Get products from iSales"""
    payload = {'username': USER,
               'password': PASSW,
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
HOST = 'https://www.isales.pepsico.com'
USER = ''
PASSW = ''

arg_parser = my_parser.create_parser_argv()
namespace = arg_parser.parse_args(sys.argv[1:])

USER = str(namespace.user).strip()
PASSW = str(namespace.passw).strip()

API = Api(HOST, USER, PASSW)

get_products()
