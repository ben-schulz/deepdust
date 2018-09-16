import os
import sys


def abs_path_to_relative(relpath):
    this_path = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(this_path, relpath))

sys.path.insert(0, abs_path_to_relative('../graph'))

import deepdust.graph.names
import deepdust.graph.namedgraph
import deepdust.graph.node

import deepdust.syntax.concrete
import deepdust.syntax.value
