import deepdust.syntax.concrete as syntax

class XsdType:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return '{}{}'.format(syntax.TYPE_PREFIX, self.name)

xsd_string = XsdType(syntax.STRING_TYPE_KEYWORD)
xsd_bool = XsdType(syntax.BOOL_TYPE_KEYWORD)

class JsonLdValue:

    def __init__(self, value, xsdtype):

        self.value = value
        self.xsdtype = xsdtype


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


    def string(s):
        return JsonLdValue(JsonLdValue.JsonString(s),
                           xsd_string)


    def __str__(self):
        return str(self.value)

    
class JsonLdList:

    def __init__(self, items):
        pass


false = JsonLdValue(JsonLdValue.JsonBool(False), xsd_bool)
true = JsonLdValue(JsonLdValue.JsonBool(True), xsd_bool)
