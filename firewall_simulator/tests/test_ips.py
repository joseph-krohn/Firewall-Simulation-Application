# tests/test_ips.py

import unittest
from firewall_simulator.ips import IPS

class TestIPS(unittest.TestCase):
    def test_process_packet(self):
        signatures = ['malware']
        ips = IPS(signatures, 'DROP')
        packet = {'payload': 'This packet contains malware'}
        self.assertEqual(ips.process_packet(packet), 'DROP')
        packet = {'payload': 'This packet is clean'}
        self.assertEqual(ips.process_packet(packet), 'ALLOW')
