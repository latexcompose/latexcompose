# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `MakeTitle`."""

from latexcompose.base import Command


class MakeTitle(Command):
    r"""Generates LaTeX command `\maketitle`."""

    def __init__(self) -> None:
        super().__init__("maketitle")
