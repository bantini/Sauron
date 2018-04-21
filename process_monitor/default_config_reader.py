"""
Read the config file to find the APIs
"""
import json

class DefaultConfigReader(object):
    def __init__(self, file_path):
        self._file_path = file_path
        self._endpoint_list = []
        with open(file_path, 'r') as reader:
            api_config = json.load(reader)
            for endpoint in api_config:
                self._endpoint_list.append(endpoint)


    @property
    def file_path(self):
        'Return the file_path of the machine'
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    @property
    def endpoint_list(self):
        'Return the file_path of the machine'
        return self._endpoint_list

    @endpoint_list.setter
    def endpoint_list(self, value):
        self._endpoint_list = value
