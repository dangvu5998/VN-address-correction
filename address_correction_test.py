import os
import unittest
from .address_correction import AddressCorrection

class AddressCorrectionTest(unittest.TestCase):
    def setUp(self):
        self.addr_corr = AddressCorrection()

    def test_address_correction(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'address_test.txt'), encoding='utf-8') as f:
            for line in f:
                wrong_address, gt_address = line.split('|')
                wrong_address = wrong_address.strip().lower()
                gt_address = gt_address.strip().lower()
                result = self.addr_corr.address_correction(wrong_address)
                corrected_address = result[0] 
                self.assertEqual(corrected_address, gt_address)

if __name__ == '__main__':
    unittest.main()
    
