import copy

import deepdust.jsonld.base as base
import deepdust.jsonld.model as model


def compact(jsonld, context=None):

    obj = base.deserialize(jsonld)
    _context = model.Context(context or obj.get('@context'))

    if '@id' in obj and 2 > len(obj):
        del(obj['@id'])

    if not _context:
        return str(obj)

    if isinstance(obj, base.LdArray):

        obj[0]['@context'] = _context.tojson()

        if 1 == len(obj):
            obj = base.JObject(obj[0])

    elif isinstance(obj, base.LdDict):

        obj['@context'] = _context.tojson()


    for k in obj.keys():

        if '@type' == k and obj[k][0] in _context.terms:
            obj[k] = _context.terms[obj[k][0]]

        value = copy.deepcopy(obj[k])

        if k not in _context.terms:

            if (isinstance(value, list)
                and 1 == len(value)):

                obj[k] = value[0]

            continue


        del(obj[k])

        if (isinstance(value, list) and 1 == len(value)):
            obj[_context.terms[k]] = value[0]

        else:
            obj[_context.terms[k]] = value


        if (isinstance(obj[_context.terms[k]], dict)):

            _vals = obj[_context.terms[k]]
            if '@type' in _vals:
                typ = _vals['@type']
                if typ in _context.terms:
                    newtyp = _context.terms[typ]

                    obj[_context.terms[k]]['@type'] = newtyp


    return str(obj)
