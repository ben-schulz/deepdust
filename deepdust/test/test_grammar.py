import unittest

import deepdust.syntax.grammar as grammar

class TestGrammar(unittest.TestCase):

    def test_jsonlddoc_rejects_malformed_json(self):

        text = '{ ok : neat'

        try:
            grammar.JsonLdDoc(text)

            msg = ("Expected '{}' raised."
                   .format(grammar.JsonError.__name__))

            self.assertTrue(False, msg)

        except grammar.JsonError:
            pass


    def test_jsonlddoc_has_keys_of_original(self):

        text = '{ "ok" : "neat", "wow" : { "awe" : "some" } }'

        result = grammar.JsonLdDoc(text)

        self.assertTrue('ok' in result)
        self.assertTrue('wow' in result)
        self.assertTrue('awe' in result['wow'])


    def test_jsonlddoc_contains_top_level_properties(self):

        prop0 = "http://example.org/foo"
        prop1 = "http://example.org/bar"
        prop2 = "http://example.org/baz"
        
        text = (
        '{'
          + '"{}": "file:///foo.txt",'.format(prop0)
          + '"{}": '.format(prop1)
            + '{ "@id": "http://example.org/bar"'
            + '}, '

          + '"{}": '.format(prop2)
            + '{ "@id": "http://example.org/baz/baz.txt"'
            + '}'
            + '}'
        )

        doc = grammar.JsonLdDoc(text)

        self.assertTrue(prop0 in doc.properties)
        self.assertTrue(prop1 in doc.properties)
        self.assertTrue(prop2 in doc.properties)


    def test_jsonlddoc_dereferences_term_in_context(self):

        text = (
            """
            {
            "@context": {
                "foo" : "http://www.example.org/foo",
                "bar" : "http://www.example.org/bar"
            },
            "data": {
                "foo": "some foo",
                "bar": "some bar",
                "baz": "something else"
                }
            }
            """
            )

        doc = grammar.JsonLdDoc(text)

        fooval = doc.context.expand("foo")
        barval = doc.context.expand("bar")

        self.assertEqual(fooval, "http://www.example.org/foo")
        self.assertEqual(barval, "http://www.example.org/bar")
