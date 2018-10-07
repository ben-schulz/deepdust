import json
import copy

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

    if _context:

        if 'list' == obj.jsontype:

            obj[0]['@context'] = _context.tojson()

            if 1 == len(obj):
                obj = base_object.Json(obj[0])

        elif 'dict' == obj.jsontype:
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
