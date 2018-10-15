import json

import deepdust.jsonld.base as base

def is_iri(x):

    return (x.startswith('http:')
            or x.startswith('https:')
            or x.startswith('ftp:'))

class Context:

    def __init__(self, mapping):

        mapping = json.loads(mapping)['@context']


        def _getid(v):

            try:
                return v['@id']

            except (TypeError, AttributeError, KeyError):
                return v


        self.terms = { _getid(v) : k
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
