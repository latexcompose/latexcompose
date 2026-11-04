# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Utilities for testing node tree traversal."""

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.composable import Composable
    from latexcompose.base.node import Node


def check_next_node(
    items: Iterator[tuple[Node, Composable | None]],
    item_cls: type[Node],
    parent_cls: type[Composable] | None,
) -> None:
    """Check the next item returned by a tree iterator.

    The function retrieves the next item from the iterator and
    checks whether the node and its parent have the expected types.

    Parameters
    ----------
    items : Iterator[tuple[Node, Composable | None]]
        Iterator returned by ``iter(Node.iter_tree())``. Each item contains
        a node and its parent. The parent is ``None`` for a root node.
    item_cls : type[Node]
        Expected type of the node.
    parent_cls : type[Composable] | None
        Expected type of the parent node, or ``None`` if the node
        is expected to have no parent.

    Raises
    ------
    AssertionError
        If the node or its parent does not have the expected type.
    StopIteration
        If the iterator contains no further items.
    """  # ruff: ignore[docstring-extraneous-exception]
    item, parent = next(items)

    assert isinstance(item, item_cls), (
        f"Expected node of type {item_cls.__name__}, "
        f"got {type(item).__name__}"
    )

    if parent_cls is None:
        assert parent is None, (
            f"Expected no parent, got {type(parent).__name__}"
        )
    else:
        assert isinstance(parent, parent_cls), (
            f"Expected parent of type {parent_cls.__name__}, "
            f"got {type(parent).__name__}"
        )


def check_end_of_items(
    items: Iterator[tuple[Node, Node | None]],
) -> None:
    """Check that a tree iterator contains no further items.

    Parameters
    ----------
    items : Iterator[tuple[Node, Node | None]]
        Iterator returned by ``Node.iter_tree()``.

    Raises
    ------
    AssertionError
        If the iterator contains another item instead of being
        exhausted.
    """  # ruff: ignore[docstring-extraneous-exception]
    with pytest.raises(StopIteration):
        next(items)
