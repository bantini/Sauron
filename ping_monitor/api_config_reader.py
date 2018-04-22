"""
Read the config file to find the APIs
"""
import json
from ping_monitor.default_config_reader import DefaultConfigReader

class ApiConfigReader(object):

    def __init__(self, file_path):
        self._file_path = file_path

    @property
    def file_path(self):
        'Return the file_path of the machine'
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    def get_default_list_apis(self):
        'Return the list of endpoints'
        default_config = DefaultConfigReader(self._file_path)
        endpoints = default_config.endpoint_list
        return endpoints

if __name__ == "__main__":
    config_reader = ApiConfigReader('/Users/nilayan/Documents/Sauron/config/config.json')
    endpoint_list = config_reader.get_default_list_apis()
    print(endpoint_list)
