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
        
        
        try:
            result = f(jelement)

        except EvalError:
            raise

        except Exception as e:
            raise EvalError(jelement) from e

        return result


    class Apply:

        def __init__(self, f):

            self.apply = f


        def then(self, other):

            return Json.Apply(
                lambda x: other.apply(self.apply(x)) )

    def abstract(self):

        return Json.Apply(lambda x: self.apply(x))


    def then(self, other):

        return (Json.Apply(
            lambda x: other.apply(self.apply(x))))


def compose(fs):

    def _compose(fs):

        if not fs:
            return Json.Apply(lambda x: x)

        this = fs.pop()
        others = _compose(fs)

        return this.then(others)

    fs.reverse()
    return _compose(fs)


def _squeeze(a):

    def __squeeze(x):

        if len(x) == 1:
            return a(x[0])
        return [ a(i) for i in x ]

    return __squeeze


squeeze = Json(
    array_f = _squeeze
)


def trans_props(f, pred=None):

    def _f_cond(k, v):

        if pred(k, v):

            return f(k)

        return k


    if pred:
        _f = _f_cond

    else:
        _f = lambda k, v: f(k)

    return Json(
        obj_f = (lambda a:
                 (lambda x: { _f(k, v) : a(v)
                              for (k,v) in x.items()}
                 ))
        )


def trans_values(f, pred=None):

    def _f_conditional(k, v):

        if pred(k, v):
            try:
                return f(v)

            except Exception as e:
                raise EvalError(v) from e

        return v

    if not pred:
        _f = f
    else:
        _f = _f_conditional

    return Json(
            obj_f = (lambda a:
                     lambda x: { k : a(_f(k, v))
                                 for (k, v) in x.items() } )
        )


def drop_properties(pred):

    return Json(
        obj_f = (lambda a:
                 lambda x: { k:v for (k,v) in x.items()
                             if pred(k,v) })
    )


class EvalError(Exception):

    def __init__(self, expr):

        self.expr = expr

    def __str__(self):

        base_error_name = type(self.__cause__).__name__

        return ("{} raised when evaluating:\n\n{}"
                .format(base_error_name, self.expr))
