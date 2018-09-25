import deepdust.datamodel.node as node

class Edge:

    def __init__(self, src, dst, prop):

        self.src = src
        self.dst = dst
        self.prop = prop

        allowed_src_types = {
            node.NodeType.IRI,
            node.NodeType.BLANK
        }

        if not self.src.nodetype in allowed_src_types:

            msg = ('Source node must be one of: {}, {}'
                   .format(*allowed_src_types))

            raise EdgeValueError(msg)


class EdgeValueError(Exception):

    def __init__(self, msg=None):

        if not msg:
            msg = 'Invalid JSON-LD edge.'

        super(EdgeValueError, self).__init__(msg)
