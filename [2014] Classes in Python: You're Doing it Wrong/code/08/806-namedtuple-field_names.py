# encoding: UTF-8

import collections

# Todas estas llamadas son equivalentes
collections.namedtuple("Punto", ["x", "y", "z"])
collections.namedtuple("Punto", "x y z")
collections.namedtuple("Punto", "x,y,z")
collections.namedtuple("Punto", "x, y, z")
