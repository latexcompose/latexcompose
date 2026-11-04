# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `TexControlWordToken`."""
import re
from typing import override

from latexcompose.exceptions.token_error import TokenInitializationError

from .tex_control_token import TexControlToken

_CONTROL_WORD = re.compile(r"[A-Za-z]+")


class TexControlWordToken(TexControlToken):
    r"""Represents a TeX control word, e.g. \def, \hello, or \section."""

    def __init__(self, name: str) -> None:
        self._validate(name)
        super().__init__(name)

    @override
    def _validate(self, name: str) -> None:
        if not _CONTROL_WORD.fullmatch(name):
            msg = f"Invalid control word name: {name}"
            raise TokenInitializationError(msg)
