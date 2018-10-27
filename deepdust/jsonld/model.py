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

        if 1 == _len and isinstance(x, list) and not x[0]:
            return True

        try:
            value = x.get('@list', None)

            if value is None:
                value = x['@set']

            if 1 == len(value) and not value[0]:
                return True

            return ("null" == value or not value)

        except (KeyError, AttributeError):
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

    if k in ctx.defns and '@container' in ctx.defns[k]:

        ctype = ctx.defns[k]['@container']

        if '@list' == ctype:
            return ldlist

        if '@set' == ctype:
            return ldset

    return None


class Context:

    class Term:

        def __init__(self, term, defn, context, prefixes=None):

            def _getdefn(v):
                try:
                    return v['@id']

                except (TypeError, KeyError):
                    return v


            def _getprefix(v):

                _is_iri = is_iri(v)

                if _is_iri:

                    if not prefixes:
                        return None

                    try:
                        prefix = next( v for (k, v) in
                                       prefixes.items()
                                       if v.startswith(k) )

                        suffix = v[ len(prefix):  ]

                        return '{}:{}'.format(prefix, suffix)

                    except StopIteration:
                        return None

                    
                tokens = v.split(':')

                if 2 > len(tokens):
                    return None

                return tokens[0]


            def _gettype(v):

                try:
                    if '@type' in v:
                        return v['@type']

                except (KeyError, TypeError):
                    return v


            self.name = term
            self.ident = _getdefn(defn)
            self.prefix = _getprefix(self.ident)
            self.ldtype = _gettype(defn)

            if self.prefix:
                suffix = self.ident.split(':')[1]
                
                self.expanded_url = (
                '{}{}'.format(context[self.prefix], suffix))

            else:
                self.expanded_url = self.ident                


    def __init__(self, mapping):

        mapping = json.loads(mapping)['@context']

        def _getid(v):

            try:
                return v['@id']

            except (TypeError, KeyError):
                return v


        self.mapping = mapping

        self.terms = { _getid(v) : k
                        for (k, v) in mapping.items() }

        self.defns = { k : v
                       for (k, v) in mapping.items() }

        self.prefixes = { v : k for (k, v) in self.defns.items()
                          if is_iri(v) }

        self._terms = [ Context.Term(k, v,
                                     mapping,
                                     prefixes=self.prefixes)

                        for (k, v) in mapping.items() ]




    def match_prefix(self, iri):

        try:
            return next( x for x in self.prefixes
                         if iri.startswith(x) )

        except StopIteration:
            return None


    def apply_prefix(self, iri):

        prefix = self.match_prefix(iri)

        if not prefix:
            return iri

        return "{}:{}".format( self.prefixes[prefix],
                               iri[ len(prefix): ] )


    def get_term(self, name):

        if self.match_prefix(name):
            _name = self.apply_prefix(name)
        else:
            _name = name

        try:
            return next(t.name for t in self._terms
                        if t.ident == _name)

        except StopIteration:
            return name


    def get_type(self, term):

        try:

            defn = self.mapping[term]
            typ = defn['@type']

        except (KeyError, TypeError):

            typ = None

        return typ


    def __str__(self):

        return str(self.defns)


    def __len__(self):

        return len(self.defns)


    def tojson(self):

        return self.defns
