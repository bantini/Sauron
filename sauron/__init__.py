
from sauron.machine_monitor import MachineMonitor
from sauron.ping_monitor import PingMonitor
from sauron.process_monitor import ProcessMonitor

from sauron.stat_aggregator import machine_stat_aggregator, ping_stat_aggregator, process_stat_aggregator
from sauron.machine_warning_generator import *
from sauron.ping_warning_generator import *
from sauron.process_warning_generator import *

class Sauron(object):

    def __init__(self):
        pass

    def get_server_stats(self):
        # Get all the stats and aggregate it
        mc_monitor = MachineMonitor()
        machine_stats = mc_monitor.get_machine_info()
        pg_monitor = PingMonitor('/Users/nilayan/Documents/Sauron/sauron/config/config.json')
        ping_stats = pg_monitor.get_ping_info()
        pc_monitor = ProcessMonitor('node')
        process_stats = pc_monitor.get_process_info()
        server_stats = (machine_stat_aggregator(machine_stats),
                        ping_stat_aggregator(ping_stats),
                        process_stat_aggregator(process_stats))
        return server_stats

    def get_cpu_health(self):
        # Print warnings and errors on the status of the CPU
        mc_monitor = MachineMonitor()
        machine_stats = mc_monitor.get_machine_info()
        cpu_warning = cpu_warning_generator(machine_stats['cpu_times'])
        if cpu_warning:
            print("Warning. CPU usage of system is exceeding idle time")
        else:
            print("CPU health is fine")

    def get_memory_health(self, threshold=None):
        # Print warnings and errors on the status of the RAM
        mc_monitor = MachineMonitor()
        machine_stats = mc_monitor.get_machine_info()
        if threshold:
            mem_threshold = threshold
        else:
            mem_threshold = 1024*1024*500 #500 MB
        memory_warning = memory_warning_generator(machine_stats['virtual_memory'], mem_threshold)
        if memory_warning:
            print("Warning. Only 500 MB of memory left")
        else:
            print("Memory health is fine")

    def get_disk_health(self, threshold=None):
        # Print warnings and errors on the status of the disk
        mc_monitor = MachineMonitor()
        machine_stats = mc_monitor.get_machine_info()
        if threshold:
            mem_threshold = threshold
        else:
            mem_threshold = 1024*1024*1024 #1 GB
        disk_warning = disk_warning_generator(machine_stats['disk_usage']['/'], mem_threshold)
        if disk_warning:
            print("Warning. Over 80 percent of disk used")
        else:
            print("Disk health is fine")

    def get_ping_health(self, config_path=None):
        # Print warnings and errors on the status of the endpoints
        try:
            if config_path:
                ping_monitor = PingMonitor(config_path)
            else:
                ping_monitor = PingMonitor('./config/config.json')
            ping_stats = ping_monitor.get_ping_info()
            api_warning_generator(ping_stats)
        except IOError:
            print("Error! Please provide correct file path to config file")

    def get_process_cpu_health(self, threshold=None):
        process_monitor = ProcessMonitor('node')
        process_stats = process_monitor.get_process_info()
        if threshold:
            cpu_threshold = threshold
        else:
            cpu_threshold = 1
        cpu_percent = process_stats['cpu_percent']
        process_cpu_percent_generator(cpu_percent, cpu_threshold)

    def get_process_memory_health(self, threshold=None):
        process_monitor = ProcessMonitor('node')
        process_stats = process_monitor.get_process_info()
        if threshold:
            process_threshold = threshold
        else:
            process_threshold = 1
        memory_percent = process_stats['memory_percent']
        process_memory_percent_generator(memory_percent, process_threshold)

if __name__ == "__main__":
    sauron = Sauron()
    mc_stats = sauron.get_server_stats()
    print(mc_stats)
