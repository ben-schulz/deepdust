import unittest

import deepdust.syntax.value as values
import deepdust.graph.names as names
import deepdust.graph.node as n

class TestNode(unittest.TestCase):

    def test_may_be_jsonld_value(self):

        v = values.JsonLdValue.false
        node = n.Node.value(v)
