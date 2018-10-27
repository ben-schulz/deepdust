import unittest

import deepdust.jsonld.base as base
import deepdust.jsonld.model as model

class TestModel(unittest.TestCase):


    def test_empty_array_is_empty_collection(self):

        self.assertTrue(model.is_empty_collection([]))


    def test_scalar_is_not_empty_collection(self):

        self.assertFalse(model.is_empty_collection(2))


    def test_empty_list_object_is_empty_collection(self):

        x = { '@list': [] }

        self.assertTrue(model.is_empty_collection(x))


    def test_list_object_with_only_null_is_empty(self):

        x = { '@list': [None] }

        self.assertTrue(model.is_empty_collection(x))


    def test_set_object_with_only_null_is_empty(self):

        x = { '@set': [None] }

        self.assertTrue(model.is_empty_collection(x))


    def test_list_with_only_null_is_empty(self):

        x = [ None ]

        self.assertTrue(model.is_empty_collection(x))


    def test_nonempty_list_object_is_not_empty_collection(self):

        x = { '@list': [ 3 ] }

        self.assertFalse(model.is_empty_collection(x))


    def test_empty_set_object_is_empty_collection(self):

        x = { '@set': [] }

        self.assertTrue(model.is_empty_collection(x))


    def test_nonempty_set_object_is_not_empty_collection(self):

        x = { '@set': [ 5 ] }

        self.assertFalse(model.is_empty_collection(x))


    def test_ldtype_literal_list_is_list(self):

        x = { 'prop': {'@list': [2,3]} }

        result = model.ldtype('prop', x['prop'])

        self.assertTrue(result is model.ldlist)


    def test_ldtype_literal_list_is_list(self):

        x = { 'prop': {'@set': [2,3]} }

        result = model.ldtype('prop', x['prop'])

        self.assertTrue(result is model.ldset)


    def test_ldtype_context_defined_list_is_list(self):

        x = { 'prop': [1,2] }

        _ctx = """
        {
          "@context": {
            "prop": {
              "@container": "@list",
              "@id": "http://example.com/prop"
            }
          }
        }
        """

        ctx = model.Context(_ctx)

        result = model.ldtype('prop', x['prop'], ctx=ctx)

        self.assertTrue(result is model.ldlist)


    def test_term_identifies_all_parts_expanded_object(self):

        context = base.deserialize("""
        {
          "@context": {
            "ex": "http://example.com/",

            "term1": {
              "@type": "ex:Type1",
              "@id": "ex:Thing1"
            }
          }
        }
        """)['@context']

        term1 = model.Context.Term('term1',
                                    context['term1'],
                                    context )

        self.assertEqual('term1', term1.name)
        self.assertEqual('ex:Thing1', term1.ident)
        self.assertEqual('ex', term1.prefix)
        self.assertEqual('ex:Type1', term1.ldtype)
        self.assertEqual('http://example.com/Thing1',
                         term1.expanded_url)


    def test_term_identifies_all_parts_prefixed_term(self):

        context = base.deserialize("""
        {
          "@context": {
            "ex": "http://example.com/",
            "term2": "ex:Thing2"
          }
        }
        """)['@context']

        term2 = model.Context.Term('term2',
                                   context['term2'],
                                   context )

        self.assertEqual('term2', term2.name)
        self.assertEqual('ex:Thing2', term2.ident)
        self.assertEqual('ex', term2.prefix)
        self.assertEqual('http://example.com/Thing2',
                         term2.expanded_url)


    def test_term_identifies_all_parts_simple_iri(self):

        context = base.deserialize(
        """
        {
          "@context": {
            "ex": "http://example.com/",
            "term3": "http://example.org/Thing3"
          }
        }
        """)['@context']

        term3 = model.Context.Term('term3',
                                    context['term3'],
                                    context )

        self.assertEqual('term3', term3.name)
        self.assertTrue(term3.prefix is None)
        self.assertEqual(term3.ident, term3.expanded_url)


    def test_context_identifies_term_by_id(self):

        context = model.Context("""
        {
          "@context": {
            "ex": "http://example.com/",

            "term1": {
              "@type": "ex:Type1",
              "@id": "ex:Thing1"
            }
          }
        }
        """)

        result = context.get_term('ex:Thing1')

        self.assertEqual('term1', result)


    def test_context_identifies_term_by_id(self):

        context = model.Context("""
        {
          "@context": {
            "ex": "http://example.com/",

            "term1": {
              "@type": "ex:Type1",
              "@id": "ex:Thing1"
            }
          }
        }
        """)

        result = context.get_term('http://example.com/Thing1')

        self.assertEqual('term1', result)
