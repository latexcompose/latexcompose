# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexNewlineToken(TexToken):
    """Token which produces a newline character."""

    def __str__(self) -> str:
        return "\n"
