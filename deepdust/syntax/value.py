import math

import deepdust.syntax.concrete as syntax

class XsdType:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return '{}{}'.format(syntax.TYPE_PREFIX, self.name)


xsd_string = XsdType(syntax.STRING_TYPE_KEYWORD)
xsd_bool = XsdType(syntax.BOOL_TYPE_KEYWORD)
xsd_double = XsdType(syntax.DOUBLE_TYPE_KEYWORD)
xsd_int = XsdType(syntax.INT_TYPE_KEYWORD)

class JsonLdValue:

    def __init__(self, value, dtype):

        self.value = value
        self.dtype = dtype


    def __str__(self):

        return str(self.value)


    class JsonBool:

        def __init__(self, value):

            self.value = value


        def true():
            return JsonBool(True)


        def false():
            return JsonBool(False)    


        def __str__(self):

            if self.value:
                return syntax.TRUE

            return syntax.FALSE

        
    class JsonString:

        def __init__(self, string):

            self.string = string

        def __str__(self):
            return self.string


    class JsonNumber:

        def __init__(self, x):

            self.number = x

        def __str__(self):

            return str(self.number)


    def __str__(self):
        return str(self.value)

    
class JsonLdList:

    def __init__(self, items):
        pass


false = JsonLdValue(JsonLdValue.JsonBool(False), xsd_bool)
true = JsonLdValue(JsonLdValue.JsonBool(True), xsd_bool)


def string(s):
    return JsonLdValue(JsonLdValue.JsonString(s), xsd_string)


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

    return JsonLdValue(JsonLdValue.JsonNumber(_n), xsd_type)
