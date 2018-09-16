
class GraphName:

    _blank_type = 'blank'
    _iri_type = 'iri'


    def __init__(self, graphid, **kwargs):

        self.graphid = graphid
        self.idtype = GraphName._blank_type


    def isblank(self):
        return GraphName._blank_type == self.idtype


    def blank(nodeid):
        return GraphName(nodeid)
