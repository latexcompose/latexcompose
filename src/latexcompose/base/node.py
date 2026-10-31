# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Node`."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from latexcompose.tokens.token import Token

    from .context import IterTokensContext, IterTreeContext


class Node(ABC):
    """Base class for all classes that make up a LaTeX document."""

    def validate(self) -> None:  # ruff: ignore[empty-method-without-abstract-decorator]
        """Validate the node."""

    def iter_tree(
        self,
        parent: Node | None,
        context: IterTreeContext,  # ruff: ignore[unused-method-argument]
    ) -> Iterable[tuple[Node, Node | None]]:
        """Iterate over the node tree.

        Parameters
        ----------
        parent : Node | None
            Parent node, or None if this is the root.
        context : IterTreeContext
            Tree traversal context.

        Yields
        ------
        tuple[Node, Node | None]
            The current node and its parent.
        """
        yield self, parent

    @abstractmethod
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterable[Token]:
        """Generate the LaTeX tokens representing this node.

        Parameters
        ----------
        context : IterTokensContext
            Token traversal context.

        Returns
        -------
        Iterable[Token]
            The iterator to iterate over the tokens.
        """
