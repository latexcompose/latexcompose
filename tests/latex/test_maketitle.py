# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Tests for class `MakeTite`."""

from latexcompose.latex import MakeTitle
from tests.utils.check_tokens import check_iter_tokens_command_without_arguments


def test_maketitle_iter_tokens() -> None:
    """Test token generation of `MakeTitle()`."""
    node = MakeTitle()
    check_iter_tokens_command_without_arguments(node)
