
class GraphName:

    _blank_type = 'blank'
    _iri_type = 'iri'


    def __init__(self, graphid, **kwargs):

        self.graphid = graphid
        self.idtype = GraphName._blank_type

        if 'nametype' in kwargs:
            self.idtype = kwargs['nametype']


    def is_blank(self):
        return GraphName._blank_type == self.idtype


    def is_iri(self):
        return GraphName._iri_type == self.idtype


    def blank(nodeid):
        return GraphName(nodeid, nametype=GraphName._blank_type)


    def iri(nodeid):
        return GraphName(nodeid, nametype=GraphName._iri_type)
