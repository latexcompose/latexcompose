# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from .tex_token import TexToken


class TexParamToken(TexToken):
    """Token for a parameter in TeX (hash tag and a number)."""

    def __init__(self, index: int) -> None:
        self._index = index

    def __str__(self) -> str:
        return "#" + str(self._index)
