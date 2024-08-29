# firewall_simulator/ids.py

class IDS:
    def __init__(self, signatures):
        self.signatures = signatures

    def detect_intrusion(self, packet):
        for signature in self.signatures:
            if signature in packet['payload']:
                return True
        return False
