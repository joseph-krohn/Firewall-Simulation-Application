# tests/test_firewall.py

import unittest
from firewall_simulator.firewall import Firewall

class TestFirewall(unittest.TestCase):
    def test_check_packet(self):
        rules = [{'ip': '192.168.0.1', 'action': 'BLOCK'}]
        firewall = Firewall(rules)
        packet = {'ip': '192.168.0.1'}
        self.assertEqual(firewall.check_packet(packet), 'BLOCK')
        packet = {'ip': '10.0.0.1'}
        self.assertEqual(firewall.check_packet(packet), 'ALLOW')
