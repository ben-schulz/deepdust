import unittest
import os

import deepdust.test

def additional_tests():

    this_suite_path = os.path.abspath(__file__)
    test_dir = os.path.dirname(this_suite_path) + '/spec'

    loader = unittest.TestLoader()
    return loader.discover(test_dir, pattern='test_*.py')
