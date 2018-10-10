import unittest
import os

import deepdust.test.spec.implemented as implemented

try:
    import deepdust.test.spec.test_compaction as compaction

except ImportError:
    print("Run 'python setup.py spec' to generate test source.")
    raise


def additional_tests():

    test_suite = unittest.TestSuite()

    test_suite.addTests([
        compaction.TestCompaction('test_{}'.format(t))
        for t in implemented.compaction
    ])

    return test_suite

