#https://stackoverflow.com/questions/2525312/measuring-ping-latency-of-a-server-python
from sauron import Sauron

# Main function call
def main():
    # Call the function to get the ping time
    sauron = Sauron()
    server_stats = sauron.get_server_stats()
    print(server_stats)
    sauron.get_cpu_health()
    sauron.get_memory_health()
    sauron.get_disk_health()
    sauron.get_ping_health()
    sauron.get_process_cpu_health()
    sauron.get_process_memory_health()
    # print(server_stats)

if __name__ == "__main__":
    main()
