# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Tests for command `Begin`."""
from latexcompose.base import Argument, IterTreeContext, Text
from latexcompose.latex import Begin
from tests.utils.check_nodes import check_end_of_items, check_next_node
from tests.utils.check_tokens import (
    check_iter_tokens_command_with_single_string_argument,
)


def test_begin_tree() -> None:
    """Test node generation of `Begin("document")`."""
    node = Begin("document")
    context = IterTreeContext()
    items = node.iter_tree(None, context)
    check_next_node(items, Begin, None)
    check_next_node(items, Argument, Begin)
    check_next_node(items, Text, Argument)
    check_end_of_items(items)


def test_begin_tokens() -> None:
    """Test token generation of `Begin("document")`."""
    node = Begin("document")
    check_iter_tokens_command_with_single_string_argument(
        node, Begin, "document",
    )
