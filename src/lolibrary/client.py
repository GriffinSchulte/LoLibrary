"""League of Legends API Client Library"""
import json

from .session import LoLibrarySession


class LoLibrary:
    """League of Legends API Client Class Wrapper"""
    def __init__(self, host, token):
        self.host = host.rstrip('/')
        self.token = token
        self.session = LoLibrarySession(self.host, self.token)

    def _get(self, endpoint, params: dict = None):
        """Private method for wrapping HTTP GET requests.
        
        args:
            endpoint (str): Endpoint URL.
            params (dict): Optional. Parameter dictionart to be passed in the URL.

        returns:
            response.text: For all successful API calls, the requests.text payload
            will be returned.
        """
        url = self.host + endpoint

        response = self.session.get(url, params=params)

        if response.status_code != 200:
            # Custom exception to be raised here.
            result = None
        else:
            result = response.text

        return result

##########################################################################
# API Methods
##########################################################################
# Category: 
# Category Description
