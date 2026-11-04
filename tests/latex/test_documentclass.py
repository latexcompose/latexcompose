# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Tests for command `DocumentClass`."""

from latexcompose.base import (
    Argument,
    IterTreeContext,
    Length,
    Option,
    OptionGroup,
    Text,
    Unit,
)
from latexcompose.latex import DocumentClass, DocumentClassName
from tests.utils.check_nodes import check_end_of_items, check_next_node
from tests.utils.check_tokens import (
    check_iter_tokens_command_with_single_string_argument,
)


def test_documentclass_with_options() -> None:
    """Test node generation of `DocumentClass`."""
    node = DocumentClass(
        DocumentClassName.STANDALONE,
        OptionGroup(
            Option("border", Length(5, Unit.PT)),
        ),
    )
    context = IterTreeContext()
    items = node.iter_tree(None, context)
    check_next_node(items, DocumentClass, None)
    check_next_node(items, OptionGroup, DocumentClass)
    check_next_node(items, Option, OptionGroup)
    check_next_node(items, Length, Option)
    check_next_node(items, Argument, DocumentClass)
    check_next_node(items, Text, Argument)
    check_end_of_items(items)


def test_documentclass_tokens() -> None:
    """Test token generation of `DocumentClass("article")`."""
    node = DocumentClass("article")
    check_iter_tokens_command_with_single_string_argument(
        node, DocumentClass, "article",
    )
