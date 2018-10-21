import json

import deepdust.jsonld.base as base

class LdType:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name


ldlist = LdType('@list')
ldset = LdType('@set')


def is_iri(x):

    if not isinstance(x, str):
        return False

    return (x.startswith('http:')
            or x.startswith('https:')
            or x.startswith('ftp:'))


def is_empty_collection(x):

    try:
        _len = len(x)

        if 0 == _len:
            return True

        try:
            value = x.get('@list', None)

            if value is None:
                value = x['@set']

            return ("null" == value or [] == value)

        except (KeyError,AttributeError):
            return False


    except TypeError:
        return False


def ldtype(k, v, ctx=None):

    if isinstance(v, dict) and '@list' in v:
        return ldlist

    if isinstance(v, dict) and '@set' in v:
        return ldset

    if isinstance(v, dict) and '@type' in v:
        return v['@type']

    if k in ctx and '@container' in ctx.defns[k]:

        ctype = ctx.defns[k]['@container']
        if '@list' == ctype:
            return ldlist
        if '@set' == ctype:
            return ldset

    return None


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
