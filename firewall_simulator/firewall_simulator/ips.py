# firewall_simulator/ips.py

class IPS:
    def __init__(self, signatures, action):
        self.signatures = signatures
        self.action = action

    def process_packet(self, packet):
        for signature in self.signatures:
            if signature in packet['payload']:
                return self.action
        return 'ALLOW'
