# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexBeginGroupToken(TexToken):
    """Token to start a new group."""

    def __str__(self) -> str:
        return "{"
