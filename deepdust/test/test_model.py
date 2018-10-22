import unittest

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
