# firewall_simulator/firewall.py

class Firewall:
    def __init__(self, rules):
        self.rules = rules

    def check_packet(self, packet):
        for rule in self.rules:
            if rule['ip'] == packet['ip']:
                return rule['action']
        return 'ALLOW'

    def add_rule(self, ip, action):
        self.rules.append({'ip': ip, 'action': action})

    def remove_rule(self, ip):
        self.rules = [rule for rule in self.rules if rule['ip'] != ip]
