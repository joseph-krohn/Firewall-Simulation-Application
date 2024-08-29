# tests/test_ids.py

import unittest
from firewall_simulator.ids import IDS

class TestIDS(unittest.TestCase):
    def test_detect_intrusion(self):
        signatures = ['malware']
        ids = IDS(signatures)
        packet = {'payload': 'This packet contains malware'}
        self.assertTrue(ids.detect_intrusion(packet))
        packet = {'payload': 'This packet is clean'}
        self.assertFalse(ids.detect_intrusion(packet))
