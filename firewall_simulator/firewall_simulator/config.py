# firewall_simulator/config.py

DEFAULT_RULES = [
    {'ip': '192.168.0.1', 'action': 'BLOCK'},
    {'ip': '10.0.0.2', 'action': 'ALLOW'}
]

DEFAULT_SIGNATURES = ['malware', 'attack']
