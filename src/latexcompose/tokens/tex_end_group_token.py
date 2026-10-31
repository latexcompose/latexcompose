# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexEndGroupToken(TexToken):
    def __str__(self) -> str:
        return "}"
