# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexCommentToken(TexToken):
    """Token which produces text."""

    def __init__(self, comment: str) -> None:
        self._comment = comment

    def __str__(self) -> str:
        return "% " + self._comment + "\n"
