import unittest

import deepdust.graph.namedgraph as n

class TestNamedGraph(unittest.TestCase):

    def test_graph_is_named(self):

        iri = 'http://www.example.com'
        graph = n.NamedGraph(iri)

        self.assertEqual(iri, str(graph.name))
