from bases.FrameworkServices.UrlService import UrlService
import logging
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.exceptions import ReceivedErrorResponseError
from jsonrpcclient.requests import Request

logger = logging.getLogger(__name__)
	

NETDATA_UPDATE_EVERY=1
priority = 90000


ORDER = [
    "block_height"
]

CHARTS = {
    "block_height": {
         "options": ["Block_Height", "Blocks", "blocks", "Validator", None, "line"]
        "lines": [
            ["block_height", "block"]
        ]
     }
}

class Service(UrlService):    
    def __init__(self, name = None, scheme="http", host="localhost", port=4467, logging=True):
        UrlService.__init__(self, configuration=configuration, name=name)
        self.url = f'{scheme}://{host}:{port}/jsonrpc'
        self.client = HTTPClient(self.url, basic_logging=logging)
        self.order = ORDER
        self.definitions = CHARTS #values to show in graphs

    def http_post(self, method, **kwargs):
        try:
          if not kwargs:              
            response = self.client.send(Request(method))
          else:
            response = self.client.send(Request(method, **kwargs))

          return response.data.result

        except ReceivedErrorResponseError as ex:
            logging.error("id: %s method: '%s' message: %s", ex.response.id, method, ex.response.message
            
    def block_height(self):
        return self.http_post("block_height")["height"]

    def logMe(self,msg):
	self.debug(msg)  

    def get_data(self):
        #The data dict is basically all the values to be represented
        # The entries are in the format: { "dimension": value}
        data = dict()
                          
        data['block_height'] = self.block_height()
            
        return data






