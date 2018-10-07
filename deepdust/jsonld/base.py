import json


def deserialize(text):

    try:
        obj = json.loads(text)

    except json.decoder.JSONDecodeError:
        raise FormatError(text)
    
    if isinstance(obj, list):
        return LdArray(obj)

    elif isinstance(obj, dict):
        return LdDict(obj)

    return obj


class JObject:

    def __init__(self, obj):

        self.obj = obj


    def __eq__(self, other):

        return (hasattr(other, 'obj')
                and self.obj == other.obj)


    def __neq__(self, other):

        return not self.__eq__(other)


    def __contains__(self, key):

        return key in self.obj


    def __getitem__(self, key):

        return self.obj[key]


    def __setitem__(self, key, value):

        self.obj[key] = value


    def __delitem__(self, key):

        del(self.obj[key])


    def __len__(self):

        return len(self.obj)


    def __str__(self):

        return str(self.obj).replace("'", '"')


    def keys(self):

        return self.obj.keys()


    def get(self, key):

        if key in self.obj:
            return self.obj[keys]

        return None


    def format(self):

        return json.dumps(self.obj, sort_keys=True, indent=4)


class LdArray(JObject):

    def __init__(self, obj):

        super(LdArray, self).__init__(obj)


class LdDict(JObject):

    def __init__(self, obj):

        super(LdDict, self).__init__(obj)


class FormatError(Exception):

    def __init__(self, text, msg=None):

        self.text = text
        super(FormatError, self).__init__(msg)


    def __str__(self):
        
        return 'Failed to deserialize:\n\n{}'.format(self.text)
