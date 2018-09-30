import os
import datetime

import deepdust.io.files as files

class TestSuite:

    def __init__(self, jsonld_text):

        self.__dict__.update(**jsonld_text)

        self.cases_path = files.relative(__name__, 'cases')

        self.cases = [TestSuite.TestCase(self.cases_path, **(c))
                      for c in jsonld_text['sequence']]


    def build_cases(self, fetch):

        def clean():

            files = os.listdir(self.cases_path)
            for f in files:
                filepath = os.path.join(self.cases_path, f)
                os.remove(filepath)

            os.rmdir(self.cases_path)

        try:
            os.mkdir(self.cases_path)

        except FileExistsError:
            clean()
            os.mkdir(self.cases_path)

        def fetch_case_part(testfile):

            fetch('{}/{}'.format(self.baseIri, testfile),
                  '{}/{}'.format(self.cases_path, testfile))

        for c in self.cases:

            fetch_case_part(c.input)
            fetch_case_part(c.context)
            fetch_case_part(c.expect)



    def __str__(self):

        test_functions = str.join('\n\n',
            [str(c) for c in self.cases])

        return (
        """#generated: {}
import unittest
import json

import deepdust.jsonld.document
import deepdust.io.files

import deepdust.test.claim as claim

class Test{}(unittest.TestCase):

{}
""").format(datetime.datetime.now(), self.name, test_functions)


    class TestCase:

        def __init__(self, cases_path, **kwargs):

            self.__dict__.update(kwargs)

            def load_from(filename):

                return (
                    ('json.load('
                     'open(deepdust.io.files.relative('
                     '__name__,'
                     '"./cases/{}")))').format(filename))
            

            self.input_expression = load_from(self.input)
            self.context_expression = load_from(self.context)
            self.output_expression = load_from(self.expect)

            self.action = 'deepdust.jsonld.document.compact'
            self.assertion = 'claim.Json.equal'

            self.testname = (self.name
                             .replace(' ', '_')
                             .replace('-', '_')
                             .replace(',', '')
                             .replace('.', '')
                             .replace("'", '')
                             .replace('"', '')
                             .replace('#', '__token_hash__')
                             .replace('@', '__token_at__')
                             .replace(':', '__token__colon_')
                             .replace('/', '__token__fslash_')
                             .replace('\\', '__token__bslash_')
                             .replace('[', '__token__lbracket_')
                             .replace(']', '__token__rbracket_')
                             .replace('(', '__token__lparen_')
                             .replace(')', '__token__rparen_'))

        def __str__(self):

            return (
                """
        def test_{}(self):

            case = {}
            expect = {}
            context = {}

            result = {}(case, context)

            {}(expect, result)
            """

            ).format(
                self.testname,
                self.input_expression,
                self.output_expression,
                self.context_expression,

                self.action,
                self.assertion)
