# from subprocess import check_output
import subprocess
import psutil

class ProcessMonitor(object):

    def __init__(self, process_name):
        self._process_name = process_name
        self._process_id = get_pid(process_name)
        p = psutil.Process(self._process_id)
        self._cpu_times = p.cpu_times()
        self._cpu_percent = p.cpu_percent()
        self._memory_info = p.memory_info()
        self._memory_full_info = p.memory_full_info()
        self._memory_percent = p.memory_percent()
        # self._io_counters = p.io_counters()
        self._open_files = p.open_files()
        self._connections = p.connections()

    def get_process_info(self):
        process_info = {}
        process_info['cpu_times'] = self._cpu_times
        process_info['cpu_percent'] = self._cpu_percent
        process_info['memory_info'] = self._memory_info
        process_info['memory_full_info'] = self._memory_full_info
        process_info['memory_percent'] = self._memory_percent
        process_info['open_files'] = self._open_files
        process_info['connections'] = self._connections
        return process_info



def get_pid(name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == name:
            return proc.info['pid']


if __name__ == "__main__":
    monitor = ProcessMonitor('node')
    process_infos = monitor.get_process_info()
    print(process_infos['cpu_times'][0])
