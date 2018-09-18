import unittest

import deepdust.graph.edge as e
import deepdust.graph.node as n
import deepdust.graph.names as names
import deepdust.syntax.value as v


class TestEdge(unittest.TestCase):


    def test_has_source_and_destination(self):

        source = n.Node.iri('http://www.example.com')
        dest = n.Node.value(v.true)
        prop = names.GraphName.iri('http://www.example.org')

        edge = e.Edge(source, dest, prop)

        self.assertEqual(source, edge.src)
        self.assertEqual(dest, edge.dst)


    def test_has_property_identifier(self):

        source = n.Node.iri('http://www.example.com')
        dest = n.Node.value(v.true)
        prop = names.GraphName.iri('http://www.example.org')

        edge = e.Edge(source, dest, prop)

        self.assertEqual(prop, edge.prop)


    def test_raise_error_on_invalid_source(self):

        source = n.Node.value(v.false)
        dest = n.Node.value(v.true)
        prop = names.GraphName.iri('http://www.example.org')

        try:
            edge = e.Edge(source, dest, prop)
            msg = 'Expected error on invalid edge definition.'
            self.assertTrue(False, msg)

        except e.EdgeValueError:
            pass

        except AssertionError:
            raise
