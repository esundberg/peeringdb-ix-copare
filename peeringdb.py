import requests
from requests.auth import HTTPBasicAuth

class PeeringDB:
    def __init__(self, **kwargs):
        self.server = kwargs.get('server')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

        self._debug = kwargs.get('debug', False)

    def debug(self, message):
        if self._debug:
            print(f'DEBUG: {message}')

    def debug_enable(self):
        self._debug=True

    def debug_disable(self):
        self._debug=False

    def _get(self, **kwargs):
        path= kwargs.get('path', '')
        params = kwargs.get('params', None)
        timeout = kwargs.get('timeout', 300)

        url = f'{self.server}/{path}'
        self.debug(f'GET URL: {url}, Params: {params}')
        response = requests.get(
            url,
            auth = HTTPBasicAuth(self.username, self.password),
            params=params,
            timeout=timeout)

        self.debug(f'Response: {response}')

        if response.status_code != 200:
            print(f'Get Query Failed: {response}')
            return False

        return response.json()

    def get_net(self, **kwargs,):
        endpoint="net"

        net_id = kwargs.get('net_id', None)
        asn = kwargs.get('asn', None)

        params={}
        if asn:
            params["asn"] = asn

        return self._get(path=endpoint, params=params)

    def get_netfac(self,**kwargs):
        endpoint="netfac"

        net_id = kwargs.get('net_id')

        params={}
        if net_id:
            params["net"] = net_id

        endpoint=f'{endpoint}'
        return self._get(path=endpoint, params=params)


    def get_ixfac(self,**kwargs):
        endpoint="ixfac"



        params={}
        fac_id = kwargs.get('fac_id', None)
        if fac_id:
            params["fac"] = fac_id

        endpoint=f'{endpoint}'
        return self._get(path=endpoint, params=params)

    def get_ix(self, **kwargs):
        endpoint="ix"

        params={}

        id = kwargs.get('id', None)
        if id:
            params["id"] = id

        endpoint=f'{endpoint}'
        return self._get(path=endpoint, params=params)

    def get_ixlan(self, **kwargs):
        endpoint="ixlan"

        params={}

        ix_id = kwargs.get('ix_id', None)
        if ix_id:
            params["ix_id"] = ix_id

        depth = kwargs.get('depth', None)
        if depth:
            params["depth"] = depth

        endpoint=f'{endpoint}'
        return self._get(path=endpoint, params=params)

    def get_netixlan(self, **kwargs):
        endpoint="netixlan"

        params={}

        ix_id = kwargs.get('ix_id', None)
        if ix_id:
            params["ix_id"] = ix_id

        asn = kwargs.get('asn', None)
        if asn:
            params["asn"] = asn

        depth = kwargs.get('depth', None)
        if depth:
            params["depth"] = depth

        endpoint=f'{endpoint}'
        return self._get(path=endpoint, params=params)