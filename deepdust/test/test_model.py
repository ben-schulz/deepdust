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


    def test_nonempty_list_object_is_not_empty_collection(self):

        x = { '@list': [ 3 ] }

        self.assertFalse(model.is_empty_collection(x))


    def test_empty_set_object_is_empty_collection(self):

        x = { '@set': [] }

        self.assertTrue(model.is_empty_collection(x))


    def test_nonempty_set_object_is_not_empty_collection(self):

        x = { '@set': [ 5 ] }

        self.assertFalse(model.is_empty_collection(x))

