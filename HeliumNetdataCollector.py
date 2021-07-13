import json

from bases.FrameworkServices.UrlService import UrlService

update_every = 5

ORDER = [
    'blockheight',
    'blockage',
]

CHARTS = {
    'blockheight': {
        'options': [None, 'Validator Height', 'count', 'miner', 'miner_blockheight', 'area'],
        'lines': [
            ['block_height', 'height', 'absolute'],
        ]
    },
    'blockage': {
        'options': [None, 'Block Age', 'age', 'miner', 'miner_blockage', 'line'],
        'lines': [
            ['block_age', 'age', 'absolute'],
        ],
    },
    
}

METHODS = {
    'getblockheight': lambda r: {
        'block_height': r['height'],
    },
    'getblockage': lambda r: {
        'info_block_age': r['block_age'],
    },
}

JSON_RPC_VERSION = '2.0'


class Service(UrlService):
    def __init__(self, configuration=None, name=None):
        UrlService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.host = self.configuration.get('host', '127.0.0.1')
        self.port = self.configuration.get('port', 4467)
        self.url = '{scheme}://{host}:{port}/jsonrpc'.format(
            scheme=self.configuration.get('scheme', 'http'),
            host=self.host,
            port=self.port,
        )
        self.method = 'POST'
        self.header = {
            'Content-Type': 'application/json',
        }

    def _get_data(self):
        #
        # Helium Miner speaks JSON-RPC version 2.0 for maximum compatibility
        #
        # 1.0 spec: https://www.jsonrpc.org/specification_v1
        # 2.0 spec: https://www.jsonrpc.org/specification
        #
        # The call documentation: ## https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc
        #
        batch = []

        for i, method in enumerate(METHODS):
            batch.append({
                'version': JSON_RPC_VERSION,
                'id': i,
                'method': method,
                'params': [],
            })

        result = self._get_raw_data(body=json.dumps(batch))

        if not result:
            return None

        result = json.loads(result.decode('utf-8'))
        data = dict()

        for i, (_, handler) in enumerate(METHODS.items()):
            r = result[i]
            data.update(handler(r['result']))
