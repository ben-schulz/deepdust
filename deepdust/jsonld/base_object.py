import json

class JSON:

    def __init__(self, obj):

        self.obj = obj


    def __eq__(self, other):

        return (hasattr(other, 'obj')
                and self.obj == other.obj)

    def __neq__(self, other):

        return not self.__eq__(other)



    def format(self):

        return json.dumps(self.obj, sort_keys=True, indent=4)
