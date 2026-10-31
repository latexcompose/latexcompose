# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexOptionalArgumentSeparatorToken(TexToken):
    """Token to separate multiple optional arguments."""

    def __str__(self) -> str:
        return ","
