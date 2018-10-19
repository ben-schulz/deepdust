import unittest
import os

import deepdust.test.spec.implemented as implemented

import deepdust.test.test_functor
import deepdust.test.test_model

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

    loader = unittest.TestLoader()

    test_suite.addTest(loader.loadTestsFromTestCase(
        deepdust.test.test_functor.TestFunctor))

    test_suite.addTest(loader.loadTestsFromTestCase(
        deepdust.test.test_model.TestModel))
    

    return test_suite
