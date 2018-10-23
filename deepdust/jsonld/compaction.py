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

    return functor.trans_values(

        lambda x: context.terms.get(x, x),

        pred=lambda k, v: isinstance(k, str)
            and isinstance(v, str)
            and k == '@type')


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
