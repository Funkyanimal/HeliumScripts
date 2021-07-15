import urlservice

import json

METHODS = {
    'block_height': lambda r: {
        'block_height': r['height'],
    },
    'getmempoolinfo': lambda r: {
        'mempool_txcount': r['size'],
    },
}

JSON_RPC_VERSION = '2.0'

batch = []

for i, method in enumerate(METHODS):
    batch.append({
        'version': JSON_RPC_VERSION,
        'id': i,
        'method': method,
        'params':[],
    })

result = json.dumps(batch)
print(result)


result = str([{"jsonrpc":"2.0","result":{"height":922261},"id":0}, {"jsonrpc":"2.0","result":{"height":922262},"id":1}, {"jsonrpc":"2.0","result":{"height":922263},"id":2}])


result = json.loads(result.decode('utf-8'))

print(result)
