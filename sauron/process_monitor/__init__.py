import subprocess
import psutil

class ProcessMonitor(object):

    def __init__(self, process_name):
        self._process_name = process_name
        self._process_ids = self.get_pid(process_name)
        print(self._process_ids)
        self.process_info = []
        for _process_id in self._process_ids:
            process_info = {}
            p = psutil.Process(_process_id)
            process_info['cpu_times'] = p.cpu_times()
            process_info['cpu_percent'] = p.cpu_percent()
            process_info['memory_info'] = p.memory_info()
            process_info['memory_full_info'] = p.memory_full_info()
            process_info['memory_percent'] = p.memory_percent()
            # self._io_counters = p.io_counters()
            process_info['open_files'] = p.open_files()
            process_info['connections'] = p.connections()
            self.process_info.append(process_info)
            """
            self._cpu_times = p.cpu_times()
            self._cpu_percent = p.cpu_percent()
            self._memory_info = p.memory_info()
            self._memory_full_info = p.memory_full_info()
            self._memory_percent = p.memory_percent()
            # self._io_counters = p.io_counters()
            self._open_files = p.open_files()
            self._connections = p.connections()
            """

    def get_process_info(self):
        """
        process_info = {}
        process_info['cpu_times'] = self._cpu_times
        process_info['cpu_percent'] = self._cpu_percent
        process_info['memory_info'] = self._memory_info
        process_info['memory_full_info'] = self._memory_full_info
        process_info['memory_percent'] = self._memory_percent
        process_info['open_files'] = self._open_files
        process_info['connections'] = self._connections
        """
        return self.process_info

    def get_pid(self, name):
        pid_list = []
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'] == name:
                pid_list.append(proc.info['pid'])
        return pid_list


if __name__ == "__main__":
    monitor = ProcessMonitor('node')
    print(monitor.get_process_info())
    # process_infos = monitor.get_process_info()
    # print(process_infos['cpu_times'][0])
