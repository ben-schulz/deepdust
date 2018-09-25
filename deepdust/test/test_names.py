import unittest

import deepdust.syntax.concrete as syntax
import deepdust.datamodel.names as names


class TestNames(unittest.TestCase):

    def test_blanknode_sets_isblank(self):

        name = names.GraphName.blank("foo")

        self.assertTrue(name.is_blank())
        self.assertFalse(name.is_iri())


    def test_iri_sets_isiri(self):

        name = names.GraphName.iri("http://www.example.com")

        self.assertTrue(name.is_iri())
        self.assertFalse(name.is_blank())


    def test_blanknode_has_spec_prefix(self):

        name = names.GraphName.blank("foo")
        self.assertTrue(str(name)
                        .startswith(
                            syntax.BLANK_NODE_ID_PREFIX))

    def test_name_init_raises_on_not_iri_or_blanknode(self):

        try:
            names.GraphName("foo")

            msg = ('Expected {} raised.'
                   .format(names.NameError.__name__))
            self.assertTrue(False, msg);

        except names.NameError:
            pass
