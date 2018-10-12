import deepdust.jsonld.base as base

class Json:

    def __init__(self, **kwargs):

        def get_function(keyword):

            def _id(x):
                return x

            return kwargs.get(keyword, _id)

        def _default_array_f(app):

            return lambda array: [ app(x) for x in array ]


        def _default_obj_f(app):

            return (lambda obj:
                    { k : app(v) for (k, v) in obj.items() })


        self.array_f = kwargs.get('array_f', _default_array_f)
        self.obj_f = kwargs.get('obj_f', _default_obj_f)

        self.string_f = get_function('string_f')
        self.int_f = get_function('int_f')
        self.real_f = get_function('real_f')
        self.bool_f = get_function('bool_f')
        self.null_f = get_function('null_f')

        self.functions = {

            type(list()) : self.array_f(self.apply),
            type(dict()) : self.obj_f(self.apply),

            type('') : self.string_f,
            type(0) : self.int_f,
            type(0.0) : self.real_f,
            type(False) : self.bool_f,
            type(None) : self.null_f
        }


    def apply(self, jelement):

        ptype = type(jelement)
        try:
            f = self.functions[ptype]

        except KeyError:
            msg = ("No operation defined for type "
                   "'{}'.".format(ptype))

            raise base.JsonTypeError(msg)
        
        
        return f(jelement)


    class Apply:

        def __init__(self, f):

            self.apply = f


    def abstract(self):

        return Json.Apply(lambda x: self.apply(x))


    def then(self, other):

        return (Json.Apply(
            lambda x: other.apply(self.apply(x))))
