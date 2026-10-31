# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexBeginOptionalArgumentToken(TexToken):
    """Token for opening a optional argument.

    This isn't a token which exists in Tex, it exists only in LaTeX.
    But for consistence we inherit from TexToken.
    """

    def __str__(self) -> str:
        return "["
