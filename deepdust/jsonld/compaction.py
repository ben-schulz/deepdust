import deepdust.jsonld.model as model
import deepdust.jsonld.functor as functor


def contextualize_props(context):

    return functor.trans_props(
        lambda x: context.terms.get(x, x) )


squeeze_lists = functor.trans_values(

    lambda x: x[0],

    pred=lambda k, v:
          ( isinstance(v, list) or k == '@type')
          and 1 == len(v) )


normalize_empty_lists = functor.trans_values(

    lambda x: [],

    pred=lambda k, v:
        ( '@list' == k and 'null' == v )
        or ( isinstance(v, list)
            and 1 == len(v)
            and v[0] is None ) )


def add_singleton_sets(context):

    return functor.trans_values(

        lambda x: [x],

        pred=lambda k, v:
            model.ldtype(k, v, context) is model.ldset
            and not isinstance(v, list)
            and not isinstance(v, dict) )


def contextualize_types(context):

    def _apply_context(k, v):

        if '@type' != k:
            return v

        if model.is_iri(v):
            return context.terms.get(v, v)

        elif isinstance(v, list):
            return [ context.terms.get(y, y)
                     for y in v ]
        else:
            msg = '@type must be single array of IRIs.'
            raise TypeError(msg)


    return functor.Json(
        obj_f=lambda a:
            lambda x: { k: a( _apply_context(k, v) )
                        for (k, v) in x.items() }
    )


nullify_nonetype = functor.Json(null_f = lambda _: "null")


drop_null = functor.drop_properties(
    lambda k,v: v is not None and "null" != v )


def drop_unmapped(context):

    return functor.drop_properties(

        lambda k,v: '@' == k[0]
                     or k in context.defns
                     or model.is_iri(k) )


def opt_empty_collection(context):

    return functor.trans_values(

        lambda x: [],

        pred=lambda k, v:
              model.is_empty_collection(v)
              and ( model.ldtype(k, v, context) is model.ldset
                    or k in context.defns )
    )


def shorten_prop_prefixes(context):
    return functor.trans_props(context.apply_prefix)


def shorten_type_prefixes(context):

    def _shorten(v):

        if isinstance(v, list):

            return [ context.apply_prefix(x)
                     for x in v ]

        return context.apply_prefix(v)

    return functor.trans_values(
        _shorten,
        pred=lambda k, v: '@type' == k or '@id' == k)
