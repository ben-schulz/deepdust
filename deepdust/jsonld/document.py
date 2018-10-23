import deepdust.jsonld.base as base
import deepdust.jsonld.functor as functor
import deepdust.jsonld.model as model

import deepdust.jsonld.compaction as compaction

def compact(jsonld, context=None):

    ldobj = base.deserialize(jsonld)

    _context = model.Context(context or ldobj.get('@context'))

    result = functor.compose([

        compaction.contextualize_props(_context),
        compaction.normalize_empty_lists,
        compaction.drop_null,
        compaction.squeeze_lists,
        compaction.contextualize_types(_context),
        compaction.drop_unmapped(_context),
        compaction.nullify_nonetype,
        compaction.opt_empty_collection(_context),
        compaction.add_singleton_sets(_context)

    ]).apply(ldobj)

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
