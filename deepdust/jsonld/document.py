import deepdust.jsonld.base as base
import deepdust.jsonld.functor as functor
import deepdust.jsonld.model as model

def compact(jsonld, context=None):

    ldobj = base.deserialize(jsonld)

    _context = model.Context(context or ldobj.get('@context'))

    if '@id' in ldobj and 2 > len(ldobj):
        del(ldobj['@id'])

    compact_props = functor.trans_props(
        lambda x: _context.terms.get(x, x))

    compact_types = functor.trans_values(
        lambda x: _context.terms.get(x, x), keys={'@type'})

    result = (compact_props
                .then(functor.squeeze
                      .then(compact_types))).apply(ldobj)

    if _context:
        result['@context'] = (
            base.deserialize(context)['@context'])

    return str(result).replace("'", '"')
