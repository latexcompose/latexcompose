# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, override

from latexcompose.tokens.enter_node_token import EnterNodeToken
from latexcompose.tokens.leave_node_token import LeaveNodeToken
from latexcompose.tokens.tex_begin_group_token import TexBeginGroupToken
from latexcompose.tokens.tex_begin_optional_argument_token import (
    TexBeginOptionalArgumentToken,
)
from latexcompose.tokens.tex_end_group_token import TexEndGroupToken
from latexcompose.tokens.tex_end_optional_argument_token import (
    TexEndOptionalArgumentToken,
)

from .container import Container

if TYPE_CHECKING:
    from collections.abc import Iterable

    from latexcompose.tokens.token import Token

    from .context import IterTokensContext
    from .node import Node


class ArgumentDelimiter(Enum):
    """Supported delimiters for LaTeX arguments."""

    BRACES = "{}"
    BRACKETS = "[]"


class Argument(Container):
    """Represents an argument of a [Command][latexcompose.base.command.Command]."""

    def __init__(
        self,
        *children: Node,
        delimiter: ArgumentDelimiter = ArgumentDelimiter.BRACES,
    ) -> None:
        super().__init__(*children)
        self._delimiter = delimiter

    @override
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterable[Token]:
        self._mount()

        yield EnterNodeToken(self)

        if self._delimiter == ArgumentDelimiter.BRACES:
            yield TexBeginGroupToken()
            yield from self._iter_children(context)
            yield TexEndGroupToken()

        elif self._delimiter == ArgumentDelimiter.BRACKETS:
            yield TexBeginOptionalArgumentToken()
            yield from self._iter_children(context)
            yield TexEndOptionalArgumentToken()

        yield LeaveNodeToken(self)
