
import unittest
import json

import deepdust.jsonld.document
import deepdust.test.claim as claim

class TestCompaction(unittest.TestCase):


        def test_drop_free_floating_nodes(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            
