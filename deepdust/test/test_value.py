import unittest

import deepdust.syntax.concrete as syntax
import deepdust.syntax.value as value


class TestJsonLdValue(unittest.TestCase):

    def test_falsevalue_has_spec_string_value(self):

        false = value.JsonLdValue.false

        self.assertEqual(syntax.FALSE, str(false))


    def test_truevalue_has_spec_true_value(self):

        true = value.JsonLdValue.true

        self.assertEqual(syntax.TRUE, str(true))
