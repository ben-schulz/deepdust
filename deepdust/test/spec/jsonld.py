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

def load_text(filename):

        f = open(deepdust.io.files.relative(__name__, "cases/" + filename))
        txt = ''
        try:
            txt = f.read()

        finally:
            f.close()

        return txt


class Test{}(unittest.TestCase):

{}
""").format(datetime.datetime.now(),
            self.name,
            test_functions)


    class TestCase:

        def __init__(self, cases_path, **kwargs):

            self.__dict__.update(kwargs)
            
            self.action = 'deepdust.jsonld.document.compact'
            self.assertion = 'claim.Json.equal'

            self.testid = kwargs['@id'].replace('#', '')

        def __str__(self):

            return (
                """
        def test_{}(self):
            \"\"\"
            {}
            \"\"\"

            case = load_text("{}")
            context = load_text("{}")
            expect = load_text("{}")

            result = {}(case, context)

            {}(expect, result)

                """

            ).format(
                self.testid,
                self.purpose,
                self.input,
                self.context,
                self.expect,

                self.action,
                self.assertion)
