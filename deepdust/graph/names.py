import deepdust.syntax.concrete as syntax

class BlankNode:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Iri:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class GraphName:

    _blank_type = 'blank'
    _iri_type = 'iri'


    def __init__(self, graphid, **kwargs):

        if isinstance(graphid, Iri):
            self.idtype = GraphName._iri_type

        elif isinstance(graphid, BlankNode):
            self.idtype = GraphName._blank_type

        else:
            raise NameError(graphid)

        self.graphid = graphid


    def __str__(self):

        _str = str(self.graphid)
        
        if self.is_blank():
            return (syntax.BLANK_NODE_ID_PREFIX + _str)

        return _str


    def is_blank(self):
        return GraphName._blank_type == self.idtype


    def is_iri(self):
        return GraphName._iri_type == self.idtype


    def blank(nodeid):
        
        blank = BlankNode(nodeid)
        return GraphName(blank)


    def iri(nodeid):

        iri = Iri(nodeid)
        return GraphName(iri)


class NameError(TypeError):

    def __init__(self, typearg):

        self.typearg = typearg

        msg = ("'{}' is not a valid type for '{}'."
               .format(
                   type(typearg).__name__,
                   GraphName.__name__))


        super(NameError, self).__init__(msg)
