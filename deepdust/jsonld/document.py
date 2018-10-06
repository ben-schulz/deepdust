import json
import deepdust.jsonld.base_object as base_object
import deepdust.jsonld.model as model


def compact(jsonld, context=None):

    obj = base_object.Json(jsonld)

    if not context:
        _context = model.Context(obj['@context'])

    else:
        _context = model.Context(context)

    if '@id' in obj and 2 > len(obj):
        del(obj['@id'])

    return str(obj)
