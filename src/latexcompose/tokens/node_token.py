# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from latexcompose.base import Node


from .token import Token


class NodeToken(Token):
    """Base class for all tokens related to node traversal."""

    def __init__(self, node: Node) -> None:
        self._node = node

    @property
    def node(self) -> Node:
        return self._node
