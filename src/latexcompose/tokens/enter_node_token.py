# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

from .node_token import NodeToken

if TYPE_CHECKING:
    from latexcompose.base.node import Node


class EnterNodeToken(NodeToken):
    """Token for beginning a new node."""

    def __init__(self, node: Node) -> None:
        super().__init__(node)
