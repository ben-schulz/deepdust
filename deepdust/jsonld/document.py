import copy

import deepdust.jsonld.base as base
import deepdust.jsonld.functor as functor
import deepdust.jsonld.model as model

def compact(jsonld, context=None):

    ldobj = base.deserialize(jsonld)

    _context = model.Context(context or ldobj.get('@context'))

    if '@id' in ldobj and 2 > len(ldobj):
        del(ldobj['@id'])

    if not _context:
        return str(ldobj)

    compact_props = functor.Json(
        obj_f = (lambda a:
                 (lambda x: { _context.terms.get(k, k) : a(v)
                              for (k,v) in x.items()}
                 ))
        )

    def unify(a):

        def _unify(x):

            if len(x) == 1:
                return a(x[0])
            return [ a(i) for i in x ]

        return _unify

    collapse_singleton_arrays = (
        functor.Json(array_f = unify))

    def ctx_types(a):

        def _ctx_types(x):

            _x = {}
            for k in x.keys():
                if '@type' == k:
                    _x[k] = _context.terms.get(x[k], x[k])
                else:
                    _x[k] = x[k]

            return { k : a(v) for (k, v) in _x.items() }

        return _ctx_types

    compact_types = (
        functor.Json(obj_f = ctx_types))

    _compact = (compact_props
                .then(collapse_singleton_arrays
                      .then(compact_types)))

    result = _compact.apply(ldobj)

    result['@context'] = base.deserialize(context)['@context']

    return str(result).replace("'", '"')
