import deepdust.jsonld.base as base

class Json:

    class NotExpectedError(AssertionError):

        def __init__(self, expect, actual, msg=None):

            self.expect = expect
            self.actual = actual
            self.msg = msg

            super(Json.NotExpectedError, self).__init__(msg)


        def __str__(self):
            
            return ('\nExpected:\n{}\n\nActual:\n{}\n'
                 .format(
                     base.show(self.expect),
                     base.show(self.actual)))


    def equal(expect, actual):

        _expect = base.deserialize(expect)
        _actual = base.deserialize(actual)

        if _expect != _actual:
            raise Json.NotExpectedError(_expect, _actual)
