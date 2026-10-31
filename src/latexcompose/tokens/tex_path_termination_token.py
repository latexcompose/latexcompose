# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexPathTerminationToken(TexToken):
    """Terminate the path specifiation in `tikz`.

    The library `tikz` is using a semicolon to terminate a path specification.
    """

    def __str__(self) -> str:
        """Return a semicolon."""  # noqa: DOC201
        return ";"
