import unittest
import sys
sys.path.append("..")

from data_structures.datacenter import Datacenter
import unittest

class Test_remove_invalid_clusters(unittest.TestCase):
    def runTest(self):
        model = Datacenter('Paris',['PAR-1','ABC-4567'])
        model.remove_invalid_clusters()
        self.assertEqual(model.cluster_list,'PAR-1')


if __name__ == '__main__':
    unittest.main()