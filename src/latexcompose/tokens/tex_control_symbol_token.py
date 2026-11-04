# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `TexControlSymbolToken`."""

import re
from typing import override

from latexcompose.exceptions.token_error import TokenInitializationError

from .tex_control_token import TexControlToken

_CONTROL_SYMBOL = re.compile(r"[\\%$#&{}_^]")


class TexControlSymbolToken(TexControlToken):
    r"""Represents a TeX control symbol, e.g. \%, \$, \{, or \}."""

    def __init__(self, symbol: str) -> None:
        self._validate(symbol)
        super().__init__(symbol)

    @override
    def _validate(self, name: str) -> None:
        if not _CONTROL_SYMBOL.fullmatch(name):
            msg = f"Invalid control symbol: {name}"
            raise TokenInitializationError(msg)
