# firewall_simulator/utils.py

def log_event(event):
    with open('event_log.txt', 'a') as f:
        f.write(f"{event}\n")
