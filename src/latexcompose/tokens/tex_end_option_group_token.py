# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexEndOptionGroupToken(TexToken):
    """Token for closing a croup of options."""

    def __str__(self) -> str:
        return "]"
