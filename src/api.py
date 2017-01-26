import requests

class Api:
    """Exchange with any Web Services"""

    def __init__(self, host, user, passw):
        self.host = host
        self.user = user
        self.passw = passw


    def execute_get_query(self, url_method, payload = {}, headers = {}):
        """Execute 'GET' query current web service"""
        try:
            result = requests.get(self.host + url_method, params=payload, headers=headers)
        except:
            return None

        return result


    def execute_post_query(self, url_method, payload = {}, headers = {}):
        """Execute 'POST' query current web service"""
        try:
            result = requests.post(self.host + url_method, data=payload, headers=headers)
        except:
            return None

        return result



