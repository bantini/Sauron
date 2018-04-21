"""
Module to monitor the API health
"""
from api_config_reader import ApiConfigReader
import requests

class PingMonitor(object):

    def __init__(self):
        apiconfig = ApiConfigReader('../config/config.json')
        endpoints = apiconfig.get_default_list_apis()
        self._endpoints_status = []
        for endpoint in endpoints:
            response_output = make_api_call(endpoint)
            self._endpoints_status.append(response_output)

    @property
    def endpoints_status(self):
        'Return the Endpoint statuses'
        return self._endpoints_status

    @endpoints_status.setter
    def endpoints_status(self, value):
        self._endpoints_status = value

    def get_endpoint_statuses(self):
        'Get the list of statuses'
        return self._endpoints_status

def make_api_call(endpoint):
    response_output = {}
    if endpoint['method'] == 'GET':
        r = requests.get(endpoint['endpoint'])
        if r.status_code == 200:
            response_output['endpoint'] = endpoint['endpoint']
            response_output['response_time'] = r.elapsed.total_seconds()
            response_output['status'] = True
        else:
            response_output['endpoint'] = endpoint['endpoint']
            response_output['response_time'] = r.elapsed.total_seconds()
            response_output['status'] = False
    else:
        # TODO: Implement for other HTTP methods
        pass
    return response_output

if __name__ == "__main__":
    monitor = ProcessMonitor()
    statuses = monitor.get_endpoint_statuses()
    print(statuses[0]['endpoint'])
    print(statuses[0]['response_time'])
    print(statuses[0]['status'])