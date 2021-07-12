from bases.FrameworkServices.UrlService import UrlService
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.exceptions import ReceivedErrorResponseError
from jsonrpcclient.requests import Request



	

NETDATA_UPDATE_EVERY=1
priority = 90000


ORDER = [
    "block_height"
]

CHARTS = {
    "block_height_chart": {
        'options': ["Block_Height", "blocks", "blocks", "Validator", "Current_Block_Height", "line"],
        "lines": [
            ["block_height","block"]
        ]
     }
}

class Service(UrlService):
    def __init__(self, scheme="http", host="localhost", port=4467, configuration=None, name=None):
        UrlService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.url = f'{scheme}://{host}:{port}/jsonrpc'
       
            
    def block_height(self):
	height = self.http_post("block_height")["height"]		  
        return height

    def logMe(self,msg):
	self.debug(msg)  

    def _get_data(self):
        data = dict()

        validatorstats = self.get_validator_stats()
        if not validatorstats:
            return None

        data.update(validatorstats)
	
    def get_validator_stats
	url = '{0}{1}'.format(self.url, '[blo
	raw = self._get_raw_data(url)
	
        data = dict()
            
        return data






