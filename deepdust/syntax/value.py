import deepdust.syntax.concrete as syntax

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


    false = JsonBool(False)
    true = JsonBool(True)

    class JsonString:

        def __init__(self, string):

            self.string = string

        def __str__(self):
            return self.string


    def string(s):
        return JsonLdValue(JsonLdValue.JsonString(s),
                           'xsd:string')


    def __str__(self):
        return str(self.value)

    
class JsonLdList:

    def __init__(self, items):
        pass
