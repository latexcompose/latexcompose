# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `TexControlToken`."""

from abc import abstractmethod

from latexcompose.tokens.tex_token import TexToken


class TexControlToken(TexToken):
    """Base class for TeX control sequences."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """The control sequence name."""
        return self._name

    def __str__(self) -> str:
        return f"\\{self._name}"

    @abstractmethod
    def _validate(self, name: str) -> None:
        """Validate the control sequence name."""
