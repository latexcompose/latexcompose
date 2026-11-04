# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexBeginOptionGroupToken(TexToken):
    """Token for opening a group of options."""

    def __str__(self) -> str:
        return "["
