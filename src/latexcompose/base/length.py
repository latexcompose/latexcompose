# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Length`."""

from typing import TYPE_CHECKING, override

from latexcompose.base.primitive import Primitive
from latexcompose.tokens import TexTextToken, Token

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.context import IterTokensContext
    from latexcompose.base.unit import Unit


class Length(Primitive):
    """Generates <value><unit>."""

    def __init__(self, value: float, unit: Unit) -> None:
        super().__init__()
        self._value = value
        self._unit = unit

    @override
    def iter_tokens(self, context: IterTokensContext) -> Iterator[Token]:
        yield TexTextToken(f"{self._value}{self._unit}")

    def __str__(self) -> str:
        """Return the length as string."""  # ruff: ignore[docstring-missing-returns]
        return f"{self._value}{self._unit}"
