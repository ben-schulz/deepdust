import json

import deepdust.jsonld.base_object as base_object

class Context:

    def __init__(self, mapping):

        mapping = json.loads(mapping)['@context']

        self.terms = { v : k
                        for (k, v) in mapping.items() }

        self.defns = { k : v
                       for (k, v) in mapping.items() }


    def __str__(self):

        return str(self.defns)


    def __len__(self):

        return len(self.defns)


    def __contains__(self, key):

        return key in self.defns.keys()


    def tojson(self):

        return self.defns
