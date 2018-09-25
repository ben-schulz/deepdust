import unittest

import deepdust.syntax.concrete as syntax
import deepdust.datamodel.value as value

import deepdust.graph.names as names


class TestJsonLdValue(unittest.TestCase):

    def test_falsevalue_has_spec_string_value(self):

        false = value.false

        self.assertEqual(syntax.FALSE, str(false))


    def test_truevalue_has_spec_true_value(self):

        true = value.true

        self.assertEqual(syntax.TRUE, str(true))


    def test_bool_is_type_xsd_bool(self):

        false = value.false
        true = value.true
        
        self.assertEqual('xsd:boolean', str(false.dtype))
        self.assertEqual('xsd:boolean', str(true.dtype))


    def test_string_is_type_xsd_string(self):

        data = 'ok'
        s = value.string(data)

        self.assertEqual(data, str(s))
        self.assertEqual('xsd:string', str(s.dtype))


    def test_number_has_equal_integer_value(self):

        data = '255'
        n = value.number(data)

        self.assertEqual(int(data), int(str(n)))


    def test_number_has_equal_fractional_value(self):

        data = '2.713'
        n = value.number(data)

        self.assertEqual(float(data), float(str(n)))


    def test_fractional_number_is_xsd_double(self):

        data = '2.713'
        n = value.number(data)

        self.assertEqual('xsd:double', str(n.dtype))


    def test_integral_number_is_xsd_integer(self):

        data = '255'
        n = value.number(data)

        self.assertEqual(255, int(str(n)))
        self.assertEqual('xsd:integer', str(n.dtype))

        
    def test_number_is_integer_if_zero_fractional_part(self):

        data = '255.0'
        n = value.number(data)

        self.assertEqual(255, int(str(n)))
        self.assertEqual('xsd:integer', str(n.dtype))


    def test_typedvalue_raises_error_on_type_not_iri(self):

        val = 'ok wow'
        typ = 'not an iri'

        try:
            x = value.typed(val, typ)

            msg = ("Expected '{}' raised."
                   .format(value.JsonLdValueError.__name__))
            self.assertTrue(False, msg)

        except value.JsonLdValueError:
            pass


    def test_typedvalue_has_iri_as_typed_member(self):

        val = 'ok wow'
        typ = 'http://www.example.com/ok#wow'

        x = value.typed(val, names.Iri(typ))

        self.assertTrue(isinstance(x.dtype, names.Iri))
