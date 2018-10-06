import json

class Json:

    def __init__(self, obj):

        if isinstance(obj, str):
            self.obj = json.loads(obj)
        else:
            self.obj = obj


    def __eq__(self, other):

        return (hasattr(other, 'obj')
                and self.obj == other.obj)

    def __neq__(self, other):

        return not self.__eq__(other)



    def format(self):

        return json.dumps(self.obj, sort_keys=True, indent=4)
