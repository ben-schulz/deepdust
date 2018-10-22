import deepdust.jsonld.base as base
import deepdust.jsonld.functor as functor
import deepdust.jsonld.model as model

def compact(jsonld, context=None):

    ldobj = base.deserialize(jsonld)

    _context = model.Context(context or ldobj.get('@context'))

    compact_props = functor.trans_props(
        lambda x: _context.terms.get(x, x))

    squeeze_lists = functor.trans_values(
            lambda x: x[0],
            pred=(lambda k, v:
                  (isinstance(v, list) or k == '@type')
                  and 1 == len(v))
            )

    normalize_empty_lists = functor.trans_values(
        lambda x: [],
        pred=lambda k, v:
            ('@list' == k and 'null' == v)
            or (isinstance(v, list)
                and 1 == len(v)
                and v[0] is None)

    )

    add_singleton_sets = functor.trans_values(
        lambda x: [x],
        pred=lambda k, v:
            model.ldtype(k, v, _context) is model.ldset
            and not isinstance(v, list)
            and not isinstance(v, dict)
    )

    compact_types = functor.trans_values(
        lambda x: _context.terms.get(x, x),
        pred=lambda k, v: isinstance(k, str)
        and isinstance(v, str)
        and k == '@type')


    nullify_nonetype = functor.Json(null_f = lambda _: "null")

    drop_null = functor.drop_properties(lambda k,v:
                                        not v is None
                                        and "null" != v)

    drop_unmapped = functor.drop_properties(
        lambda k,v: ('@' == k[0]
                     or k in _context.defns
                     or model.is_iri(k)))

    opt_empty_collection = functor.trans_values(lambda x: [],
        pred=(lambda k, v:
              model.is_empty_collection(v)
              and (model.ldtype(k,v,_context) is model.ldset
                   or k in _context.defns))
    )

    result = (
        compact_props
        .then(normalize_empty_lists
        .then(drop_null
        .then(squeeze_lists
        .then(compact_types

        .then(drop_unmapped

        .then(nullify_nonetype

        .then(opt_empty_collection



        .then(add_singleton_sets

        ))))))))).apply(ldobj)

    if '@id' in result and 2 > len(result):
        del(result['@id'])

    if _context:

        if isinstance(result, list):
            result[0]['@context'] = (
                base.deserialize(context)['@context'])

        else:
            result['@context'] = (
                base.deserialize(context)['@context'])


    if isinstance(result, list) and 1 == len(result):
        result = result[0]

    return str(result).replace("'", '"')
