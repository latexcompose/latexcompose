# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from abc import abstractmethod

from .token import Token


class TexToken(Token):
    """Base class for all TeXTokens."""

    @abstractmethod
    def __str__(self) -> str: ...
