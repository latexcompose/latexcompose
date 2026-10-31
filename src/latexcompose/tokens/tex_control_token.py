# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

import re

from latexcompose.exceptions.token_error import TokenInitializationError

from .tex_token import TexToken

_CONTROL_WORD = re.compile(r"[A-Za-z]+")
_CONTROL_SYMBOL = re.compile(r"[\\%$#&{}_^]")


def is_valid_control_token_string(text: str) -> bool:
    """Return true if text is a valid control word or control symbol.

    Parameters
    ----------
    text : str
        The text which will be checked.

    Returns
    -------
    bool
        Return true if text is a valid control word or control symbol.
    """
    return bool(
        _CONTROL_SYMBOL.fullmatch(text) or _CONTROL_WORD.fullmatch(text),
    )


class TexControlToken(TexToken):
    r"""Represents a TeX control word or symbol, e.g., \def, \hello, \section."""  # ruff: ignore[line-too-long]

    def __init__(self, name: str):
        if not is_valid_control_token_string(name):
            msg = f"Invalid token name: {name}"
            raise TokenInitializationError(msg)
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        return f"\\{self._name}"
