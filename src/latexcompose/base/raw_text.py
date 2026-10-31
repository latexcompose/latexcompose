# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT


from typing import TYPE_CHECKING

from latexcompose.base.context import IterTokensContext
from latexcompose.base.primitive import Primitive
from latexcompose.tokens import TexTextToken, Token

if TYPE_CHECKING:
    from collections.abc import Iterator


class RawText(Primitive):
    def __init__(self, text: str) -> None:
        self._text = text

    def iter_tokens(self, context: IterTokensContext) -> Iterator[Token]:
        yield TexTextToken(self._text)
