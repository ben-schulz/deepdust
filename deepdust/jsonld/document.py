import deepdust.jsonld.base as base
import deepdust.jsonld.functor as functor
import deepdust.jsonld.model as model

def compact(jsonld, context=None):

    ldobj = base.deserialize(jsonld)

    _context = model.Context(context or ldobj.get('@context'))

    compact_props = functor.trans_props(
        lambda x: _context.terms.get(x, x))

    compact_types = functor.trans_values(
        lambda x: _context.terms.get(x, x),
        pred=lambda k, v: k in {'@type'} )

    nullify_nonetype = functor.Json(null_f = lambda _: "null")

    drop_null = functor.drop_properties(lambda k,v: None != v)

    drop_unmapped = functor.drop_properties(
        lambda k,v: ('@' == k[0]
                     or k in _context.defns
                     or model.is_iri(k)))

    opt_empty_set = functor.trans_values(lambda x: [],
        pred=lambda k,v: ('@set' in v
                          and len(v['@set']) == 0))

    opt_empty_set0 = functor.trans_values(lambda x: [],
        pred=lambda k,v: ('@set' in v and "null" == v['@set']))

    opt_empty_list = functor.trans_values(lambda x: [],
        pred=lambda k,v: '@list' in v and not v['@list'])

    opt_empty_list0 = functor.trans_values(lambda x: [],
        pred=lambda k,v: '@list' in v and "null" == v['@list'])

    result = (
        compact_props
        .then(functor.squeeze
        .then(compact_types
        .then(drop_null
        .then(drop_unmapped
        .then(nullify_nonetype
        .then(opt_empty_set
        .then(opt_empty_set0
        .then(opt_empty_list
        .then(opt_empty_list0
        )))))))))).apply(ldobj)

    if '@id' in result and 2 > len(result):
        del(result['@id'])

    if _context:
        result['@context'] = (
            base.deserialize(context)['@context'])

    return str(result).replace("'", '"')
