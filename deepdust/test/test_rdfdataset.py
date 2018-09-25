import unittest

import deepdust.datamodel.rdfdataset as rdf

class TestNamedGraph(unittest.TestCase):

    def test_graph_is_named(self):

        iri = 'http://www.example.com'
        graph = rdf.NamedGraph(iri)

        self.assertEqual(iri, str(graph.name))
