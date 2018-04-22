"""
Helper functions to format the data in a relevant format
"""

def machine_stat_aggregator(machine_stats):
    # Format the Machine stats
    return {"machine_stats": machine_stats}

def ping_stat_aggregator(ping_stats):
    # Format the ping stats
    return {"ping_stats": ping_stats}

def process_stat_aggregator(process_stats):
    # Format the process stats
    return {"process_stats": process_stats}
