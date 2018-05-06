from subprocess import call
import psutil

def get_v8_heap(path_to_file=None):
    if path_to_file is None:
        path_to_file = "/Users/nilayan/Documents/Sauron/saruman/executor.js"
    try:
        call(["node", path_to_file])
    except psutil.AccessDenied:
        print("Please run the script as admin")
    except IOError:
        print("Please enter a valid path for the Saruman executor nodejs script.")



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
        get_v8_heap()
    else:
        print(" Process Memory usage under control")

if __name__ == "__main__":
    get_v8_heap('random')
