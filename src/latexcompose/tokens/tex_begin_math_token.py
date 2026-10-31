# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexBeginMathToken(TexToken):
    """Token to start a math environment."""

    def __str__(self) -> str:
        return "$"
