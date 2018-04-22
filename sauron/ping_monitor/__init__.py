"""
Module to monitor the API health
"""
from sauron.ping_monitor.api_config_reader import ApiConfigReader
import requests

class PingMonitor(object):

    def __init__(self, config_path):
        apiconfig = ApiConfigReader(config_path)
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

    def get_ping_info(self):
        'Get the list of statuses'
        return self._endpoints_status

def make_api_call(endpoint):
    response_output = {}
    try:
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
    except requests.exceptions.ConnectionError:
        response_output['endpoint'] = endpoint['endpoint']
        response_output['response_time'] = 99999
        response_output['status'] = False
    return response_output

if __name__ == "__main__":
    monitor = PingMonitor('/Users/nilayan/Documents/Sauron/sauron/config/config.json')
    statuses = monitor.get_ping_info()
    print(statuses[0]['endpoint'])
    print(statuses[0]['response_time'])
    print(statuses[0]['status'])
