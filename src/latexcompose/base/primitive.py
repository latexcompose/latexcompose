# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .node import Node


class Primitive(Node):
    """Base class for all nodes that don't have children."""
