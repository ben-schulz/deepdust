import math

import deepdust.syntax.concrete as syntax
import deepdust.graph.names as names

class Type:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return '{}'.format(self.name)

    def xsd(name):

        return Type(syntax.XSD_TYPE_PREFIX + name)


xsd_string = Type.xsd(syntax.STRING_TYPE_KEYWORD)
xsd_bool = Type.xsd(syntax.BOOL_TYPE_KEYWORD)
xsd_double = Type.xsd(syntax.DOUBLE_TYPE_KEYWORD)
xsd_int = Type.xsd(syntax.INT_TYPE_KEYWORD)

class JsonLdValue:

    def __init__(self, value, dtype):

        self.value = value
        self.dtype = dtype


    def __str__(self):

        return str(self.value)


    class Bool:

        def __init__(self, value):

            self.value = value


        def true():
            return Bool(True)


        def false():
            return Bool(False)    


        def __str__(self):

            if self.value:
                return syntax.TRUE

            return syntax.FALSE

        
    class String:

        def __init__(self, string):

            self.string = string

        def __str__(self):
            return self.string


    class Number:

        def __init__(self, x):

            self.number = x

        def __str__(self):

            return str(self.number)


    def __str__(self):
        return str(self.value)


    class Typed:

        def __init__(self, val, typ):

            self.val = val
            self.typ = typ

    
class JsonLdList:

    def __init__(self, items):
        pass


false = JsonLdValue(JsonLdValue.Bool(False), xsd_bool)
true = JsonLdValue(JsonLdValue.Bool(True), xsd_bool)


def string(s):
    return JsonLdValue(JsonLdValue.String(s), xsd_string)


def number(n):

    try:
        _n = int(n)
        xsd_type = xsd_int

    except ValueError:

        _n = float(n)

        if math.floor(_n) < _n:
            xsd_type = xsd_double
        else:
          _n = int(math.floor(_n))
          xsd_type = xsd_int

    return JsonLdValue(JsonLdValue.Number(_n), xsd_type)


def typed(v, t):

    if not isinstance(t, names.Iri):
        raise JsonLdValueError(t)

    return JsonLdValue(JsonLdValue.Typed(v, t), t)


class JsonLdValueError(Exception):

    def __init__(self, typearg):

        self.typearg = typearg

        msg = ("'{}' is not a valid type for '{}'."
               .format(
                   type(typearg).__name__,
                   JsonLdValue.Typed.__name__
                   ))

        super(JsonLdValueError, self).__init__(msg)
