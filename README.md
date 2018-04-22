# Sauron
Application and system monitoring. It uses the psutils library to generate system and process status, and requests to check API status.

# Installation
Run the following command from the sauron directory:
```
python setup.py install
```
# Usage
To retrive all the stats.
```
from sauron import Sauron
sauron = Sauron()
server_stats = sauron.get_server_stats()
```
To get CPU health of the server machine i.e. if the total time spent in processing is more than the idle time.
```
sauron.get_cpu_health()
```
To get the memory health, where the used memory does not exceed a user specified threshold in bytes. The default is 500 MB.
```
sauron.get_memory_health(threshold)
```
To get the disk health, where the used disk space does not exceed a user specified threshold in bytes. The default is 1 GB.
```
sauron.get_disk_health(threshold)
```
To get the ping health, the user has to provide a config file. Right now, it is working only for GET requests.
```
sauron.get_ping_health(config_file)
```
The format of the config file is as follows:
```
[{"endpoint":"http://www.test.com/", "method": "GET"}, {"endpoint":"http://www.nilayan.com", "method": "GET"}]
```

