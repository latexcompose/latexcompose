# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Command`."""

from typing import TYPE_CHECKING, override

from latexcompose.tokens import (
    EnterNodeToken,
    LeaveNodeToken,
    TexControlToken,
    Token,
)

from .container import Container

if TYPE_CHECKING:
    from collections.abc import Iterable

    from .argument import Argument
    from .context import IterTokensContext


class Command(Container):
    """Base class for all commands."""

    def __init__(
        self,
        name: str,
        *arguments: Argument,
    ) -> None:
        """Initialize instance attributes.

        Parameters
        ----------
        name : str
            Command name.
        """
        super().__init__(*arguments)
        self._name = name

    @override
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterable[Token]:
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
        yield TexControlToken(self._name)
        yield from self._iter_children(context)
        yield LeaveNodeToken(self)
