# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Composable`."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from latexcompose.base.composable import Composable
from latexcompose.base.group_delimiter import GroupDelimiter
from latexcompose.tokens import TexBeginOptionGroupToken, TexEndOptionGroupToken
from latexcompose.tokens.enter_node_token import EnterNodeToken
from latexcompose.tokens.leave_node_token import LeaveNodeToken
from latexcompose.tokens.tex_begin_group_token import TexBeginGroupToken
from latexcompose.tokens.tex_end_group_token import TexEndGroupToken

if TYPE_CHECKING:
    from collections.abc import Iterable

    from latexcompose.tokens.token import Token

    from .context import IterTokensContext
    from .node import Node


class Argument(Composable):
    """Represents an argument of a [Command][latexcompose.base.command.Command]."""

    def __init__(
        self,
        *children: Node,
        delimiter: GroupDelimiter = GroupDelimiter.BRACES,
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

        if self._delimiter == GroupDelimiter.BRACES:
            yield TexBeginGroupToken()
            yield from super().iter_tokens(context)
            yield TexEndGroupToken()

        elif self._delimiter == GroupDelimiter.BRACKETS:
            yield TexBeginOptionGroupToken()
            yield from super().iter_tokens(context)
            yield TexEndOptionGroupToken()

        yield LeaveNodeToken(self)
