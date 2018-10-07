import json


class Json:

    def __init__(self, obj):

        if isinstance(obj, str):

            try:
                self.obj = json.loads(obj)

            except json.decoder.JSONDecodeError:
                raise FormatError(obj)

        else:
            self.obj = obj

        if isinstance(self.obj, list):
            self.jsontype = 'list'

        elif isinstance(self.obj, dict):
            self.jsontype = 'dict'

        else:
            self.jsontype = 'undefined'



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


    def format(self):

        return json.dumps(self.obj, sort_keys=True, indent=4)


class FormatError(Exception):

    def __init__(self, text, msg=None):

        self.text = text
        super(FormatError, self).__init__(msg)


    def __str__(self):
        
        return 'Failed to deserialize:\n\n{}'.format(self.text)
