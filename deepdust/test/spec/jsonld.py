import os

class TestSuite:

    def __init__(self, jsonld_text):

        self.__dict__.update(**jsonld_text)

        this_module_path = os.path.abspath(__file__)
        this_module_dir = os.path.dirname(this_module_path)
        self.cases_path = os.path.join(this_module_dir,
                                       'cases')

        self.cases = [TestSuite.TestCase(self.cases_path, **(jsonld_text['sequence'][0]))]


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
        """
import unittest
import json

import deepdust.jsonld.document
import deepdust.test.claim as claim

class Test{}(unittest.TestCase):

{}
""").format(self.name, test_functions)


    class TestCase:

        def __init__(self, cases_path, **kwargs):

            self.__dict__.update(kwargs)
            self.cases_path = cases_path

            def load_expression(filename):
                
                path = os.path.join(self.cases_path,
                                             filename)
                return ('json.load(open("{}"))'
                        .format(path))

            self.input_expression = load_expression(
                self.input)

            self.context_expression = load_expression(
                self.context)

            self.output_expression = load_expression(
                self.expect)

            self.action = 'deepdust.jsonld.document.compact'
            self.assertion = 'claim.Json.equal'

            self.testname = (self.name
                             .replace(' ', '_')
                             .replace('-', '_'))


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
