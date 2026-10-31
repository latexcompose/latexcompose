# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexEndMathToken(TexToken):
    """Token to end a math environment."""

    def __str__(self) -> str:
        return "$"
