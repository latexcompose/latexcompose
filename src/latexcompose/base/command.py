# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Command`."""

from typing import TYPE_CHECKING, override

from latexcompose.base.composable import Composable
from latexcompose.tokens import (
    EnterNodeToken,
    LeaveNodeToken,
    TexControlToken,
    Token, TexControlWordToken,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.node import Node

    from .context import IterTokensContext


class Command(Composable):
    """Base class for all commands."""

    def __init__(
        self,
        name: str,
        *arguments: Node,
    ) -> None:
        """Initialize instance attributes.

        Parameters
        ----------
        name : str
            Command name.
        *arguments : Node
            The arguments of the command. These should be a instance of
            [Argument][latexcompose.base.Argument] or a
            [OptionGroup][latexcompose.base.OptionGroup].
        """
        super().__init__(*arguments)
        self._name = name

    @property
    def name(self) -> str:
        """Name of the command."""
        return self._name

    @override
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterator[Token]:
        """Generate tokens representing the command.

        Parameters
        ----------
        context : IterTokensContext
            Token generation context.

        Yields
        ------
        Token
            Tokens representing the command and its arguments.
        """
        self._mount()

        yield EnterNodeToken(self)
        yield TexControlWordToken(self._name)
        yield from self._iter_children(context)
        yield LeaveNodeToken(self)
