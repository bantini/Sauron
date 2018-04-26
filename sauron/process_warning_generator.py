def process_cpu_percent_generator(cpu_percent, threshold=2):
    # Print warning if CPU usage percentage crosses user threshold
    if cpu_percent > threshold:
        print("Warning. CPU usage has crossed the threshold of {threshold}%".format(threshold=threshold))
    else:
        print(" Process CPU usage under control")

def process_memory_percent_generator(memory_percent, threshold=2):
    # Print warning if Memory usage percentage crosses user threshold
    if memory_percent > threshold:
        print("Warning. Memory usage has crossed the threshold of {threshold}%".format(threshold=threshold))
    else:
        print(" Process Memory usage under control")
