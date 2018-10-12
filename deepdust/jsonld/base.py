import json

def deserialize(text):

    try:
        obj = json.loads(text)

    except json.decoder.JSONDecodeError:
        raise FormatError(text)

    return obj


def serialize(ldobj):

    return json.dumps(ldobj)


def show(ldobj):

    return json.dumps(ldobj, sort_keys=True, indent=4)


class FormatError(Exception):

    def __init__(self, text, msg=None):

        self.text = text
        super(FormatError, self).__init__(msg)


    def __str__(self):

        return 'Failed to deserialize:\n\n{}'.format(self.text)


class JsonTypeError(TypeError):

    def __init__(self, msg):

        self.msg = msg

        super(JsonTypeError, self).__init__(msg)
