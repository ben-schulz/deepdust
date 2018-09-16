import deepdust.syntax.concrete as syntax

class JsonLdValue:

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

    def __init__(self):
        pass

    
class JsonLdList:

    def __init__(self, items):
        pass
