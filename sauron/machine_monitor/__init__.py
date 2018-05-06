"""
Module to monitor the parameters of the machine
"""

import psutil

class MachineMonitor(object):

    """
    CPU_TIMES = psutil.cpu_times()
    VIRTUAL_MEMORY = psutil.virtual_memory()
    SWAP_MEMORY = psutil.swap_memory()
    DISK_PARTITIONS = psutil.disk_partitions()
    DISK_USAGE = psutil.disk_usage('/')
    NET_IO_COUNTERS = psutil.net_io_counters(pernic=True)
    """

    def __init__(self):
        self._cpu_times = psutil.cpu_times()
        self._virtual_memory = psutil.virtual_memory()
        self._swap_memory = psutil.swap_memory()
        self._disk_partitions = psutil.disk_partitions()
        self._disk_usage = psutil.disk_usage('/') # Used, free
        self._net_io_counters = psutil.net_io_counters(pernic=True)

    @property
    def cpu_times(self):
        'Return the CPU of the machine'
        return self._cpu_times

    @cpu_times.setter
    def cpu_times(self, value):
        self._cpu_times = value

    @property
    def virtual_memory(self):
        'Return the virtual memory of the machine'
        return self._virtual_memory

    @virtual_memory.setter
    def virtual_memory(self, value):
        self._virtual_memory = value

    @property
    def swap_memory(self):
        return self._swap_memory

    @swap_memory.setter
    def swap_memory(self, value):
        self._swap_memory = value

    @property
    def disk_usage(self):
        'Return the disk usage of root directory'
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, value):
        self._disk_usage = value

    def get_disk_usage(self, partition):
        # Get the disk usage of a particular partition
        return psutil.disk_usage(partition)

    def get_machine_info(self):
        # Get the statistics associated with a machine
        machine_stats = {}
        machine_stats['cpu_times'] = self._cpu_times
        machine_stats['virtual_memory'] = self._virtual_memory
        machine_stats['swap_memory'] = self._swap_memory
        disk_usage = {}
        for partitions in self._disk_partitions:
            disk_usage[partitions[1]] = self.get_disk_usage(partitions[0])
        machine_stats['disk_usage'] = disk_usage
        return machine_stats

if __name__ == "__main__":
    machine_monitor = MachineMonitor()
    out = machine_monitor.get_machine_info()
    print(out)
