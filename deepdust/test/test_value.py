import unittest

import deepdust.syntax.concrete as syntax
import deepdust.syntax.value as value


class TestJsonLdValue(unittest.TestCase):

    def test_falsevalue_has_spec_string_value(self):

        false = value.false

        self.assertEqual(syntax.FALSE, str(false))


    def test_truevalue_has_spec_true_value(self):

        true = value.true

        self.assertEqual(syntax.TRUE, str(true))


    def test_bool_has_typedvalue_xsd_bool(self):

        false = value.false
        true = value.true
        
        self.assertEqual('xsd:boolean', str(false.xsdtype))
        self.assertEqual('xsd:boolean', str(true.xsdtype))


    def test_string_is_typedvalue_xsd_string(self):

        stringvalue = 'ok'
        s = value.JsonLdValue.string(stringvalue)

        self.assertEqual(stringvalue, str(s))
        self.assertEqual('xsd:string', str(s.xsdtype))
