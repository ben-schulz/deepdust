import json

class JsonError(Exception):
    pass

class NodeObject:
    pass

class Context:

    def __init__(self, context):

        self.context = context

    def expand(self, term):

        return self.context[term];


class JsonLdDoc:

    def __getitem__(self, key):

        return self.json[key]


    def __contains__(self, key):

        return key in self.json


    def __init__(self, text):

        self.text = text

        try:
            self.json = json.loads(text)

            if not "@context" in self.json:
                self.context = {}
                self.context = Context({})
            else:
                self.context = self.json["@context"]
                self.context = Context(self.context)

            self.properties = self.json.keys()

        except:
            raise JsonError
    
