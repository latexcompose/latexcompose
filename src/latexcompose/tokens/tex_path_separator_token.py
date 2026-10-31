# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexPathSeparatorToken(TexToken):
    """Separate path operations in a `tikz` path specification.

    The library `tikz` uses spaces to separate operations in a path
    specificaton using a space character.
    """

    def __str__(self) -> str:
        """Return space character."""  # noqa: DOC201
        return " "
