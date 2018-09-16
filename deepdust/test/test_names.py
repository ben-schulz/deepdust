import unittest

import deepdust.graph.names as N

class TestNames(unittest.TestCase):

    def test_blanknode_sets_isblank(self):

        name = N.GraphName.blank("some_id")

        self.assertTrue(name.is_blank())
        self.assertFalse(name.is_iri())


    def test_iri_sets_isiri(self):

        name = N.GraphName.iri("http://www.example.com")

        self.assertTrue(name.is_iri())
        self.assertFalse(name.is_blank())
