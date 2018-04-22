
def cpu_warning_generator(cpu_tuple):
    # Returns boolean value false if used cycles is greater than idle cycles
    used_time = cpu_tuple.user + cpu_tuple.nice + cpu_tuple.system
    if used_time > cpu_tuple.idle:
        return True
    else:
        return False

def memory_warning_generator(memory_tuple):
    # Returns boolean value false if memory is less than 500 MB
    THRESHOLD = 1024*1024*500
    if memory_tuple.available <= THRESHOLD:
        return True
    else:
        return False

def disk_warning_generator(disk_tuple):
    # Returns boolean value false if disk space is less than 1 GB
    if disk_tuple.percent > 80:
        return True
    else:
        return False
