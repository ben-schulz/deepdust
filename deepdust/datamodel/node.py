from enum import Enum

class NodeType(Enum):
    VALUE = 0
    IRI = 1
    BLANK = 2
    LIST = 3


class Node:

    def __init__(self, ntype):

        self.nodetype = ntype


    def iri(v):

        return Node(NodeType.IRI)


    def blank(v):

        return Node(NodeType.BLANK)


    def value(v):

        return Node(NodeType.VALUE)


    def listnode(items):

        return Node(NodeType.LIST)
