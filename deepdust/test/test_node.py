import unittest

import deepdust.syntax.value as values
import deepdust.graph.names as names
import deepdust.graph.node as n

class TestNode(unittest.TestCase):


    def test_may_be_jsonld_value(self):

        v = values.JsonLdValue.false
        node = n.Node.value(v)

        self.assertIsNotNone(node)
        self.assertEqual(n.NodeType.VALUE, node.nodetype)


    def test_may_be_iri(self):

        name = names.GraphName.iri('http://www.example.com')
        node = n.Node.iri(name)

        self.assertIsNotNone(node)
        self.assertEqual(n.NodeType.IRI, node.nodetype)


    def test_may_be_blank(self):

        name = names.GraphName.blank('foo')
        node = n.Node.blank(name)

        self.assertIsNotNone(node)
        self.assertEqual(n.NodeType.BLANK, node.nodetype)

    def test_may_be_list(self):

        l = values.JsonLdList(['item0', 'item1'])
        node = n.Node.listnode(l)

        self.assertIsNotNone(node)
        self.assertEqual(n.NodeType.LIST, node.nodetype)
