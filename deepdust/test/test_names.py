import unittest

import deepdust.graph.names as N

class TestNames(unittest.TestCase):

    def test_blanknode_sets_isblank(self):

        name = N.GraphName.blank("some_id")

        self.assertTrue(name.isblank)
