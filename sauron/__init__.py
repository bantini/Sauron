from machine_monitor import MachineMonitor
from ping_monitor import PingMonitor
from process_monitor import ProcessMonitor

from stat_aggregator import machine_stat_aggregator, ping_stat_aggregator, process_stat_aggregator
# import ping_monitor
# import process_monitor

class Sauron(object):

    def __init__(self):
        pass

    def get_server_stats(self):
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

if __name__ == "__main__":
    sauron = Sauron()
    mc_stats = sauron.get_server_stats()
    print(mc_stats)
