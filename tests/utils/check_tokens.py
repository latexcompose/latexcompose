# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Utilities for testing token generation."""

from typing import TYPE_CHECKING

import pytest

from latexcompose.base import Argument, Command, IterTokensContext, Node, Text
from latexcompose.tokens import (
    EnterNodeToken,
    LeaveNodeToken,
    TexBeginGroupToken,
    TexControlWordToken,
    TexEndGroupToken,
    TexTextToken,
    Token,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


def check_next_enter_node_token(
    iter_tokens: Iterator[Token],
    node_cls: type[Node],
) -> None:
    """Check the next token is an EnterNodeToken.

    The function retrieves the next token and verifies that it is
    an instance of ``EnterNodeToken`` and references a node of the
    expected type.

    Parameters
    ----------
    iter_tokens : Iterator[Token]
        Iterator producing the tokens to check.
    node_cls : type[Node]
        Expected type of the node referenced by the token.

    Raises
    ------
    AssertionError
        If the next token is not an ``EnterNodeToken`` or references
        a node of an unexpected type.
    StopIteration
        If the iterator contains no further tokens.
    """  # ruff: ignore[docstring-extraneous-exception]
    token = next(iter_tokens)

    assert isinstance(token, EnterNodeToken), (
        f"Expected EnterNodeToken, got {type(token).__name__}"
    )
    assert isinstance(token.node, node_cls), (
        f"Expected node of type {node_cls.__name__}, "
        f"got {type(token.node).__name__}"
    )


def check_next_leave_node_token(
    iter_tokens: Iterator[Token],
    node_cls: type[Node],
) -> None:
    """Check the next token is a LeaveNodeToken.

    The function retrieves the next token and verifies that it is
    an instance of ``LeaveNodeToken`` and references a node of the
    expected type.

    Parameters
    ----------
    iter_tokens : Iterator[Token]
        Iterator producing the tokens to check.
    node_cls : type[Node]
        Expected type of the node referenced by the token.

    Raises
    ------
    AssertionError
        If the next token is not a ``LeaveNodeToken`` or references
        a node of an unexpected type.
    StopIteration
        If the iterator contains no further tokens.
    """  # ruff: ignore[docstring-extraneous-exception]
    token = next(iter_tokens)

    assert isinstance(token, LeaveNodeToken), (
        f"Expected LeaveNodeToken, got {type(token).__name__}"
    )
    assert isinstance(token.node, node_cls), (
        f"Expected node of type {node_cls.__name__}, "
        f"got {type(token.node).__name__}"
    )


def check_next_tex_token(
    iter_tokens: Iterator[Token],
    string: str,
    token_cls: type[Token],
) -> None:
    """Check the next token has the expected text and type.

    The function retrieves the next token and verifies both its
    string representation and its type.

    Parameters
    ----------
    iter_tokens : Iterator[Token]
        Iterator producing the tokens to check.
    string : str
        Expected string representation of the token.
    token_cls : type[Token]
        Expected type of the token.

    Raises
    ------
    AssertionError
        If the next token has an unexpected string representation
        or type.
    StopIteration
        If the iterator contains no further tokens.
    """  # ruff: ignore[docstring-extraneous-exception]
    token = next(iter_tokens)

    assert str(token) == string, (
        f"Expected token string {string!r}, got {str(token)!r}"
    )
    assert isinstance(token, token_cls), (
        f"Expected token of type {token_cls.__name__}, "
        f"got {type(token).__name__}"
    )


def check_end_of_tokens(iter_tokens: Iterator[Token]) -> None:
    """Check that a token iterator contains no further tokens.

    Parameters
    ----------
    iter_tokens : Iterator[Token]
        Iterator producing the tokens to check.

    Raises
    ------
    AssertionError
        If the iterator contains another token instead of being
        exhausted.
    """  # ruff: ignore[docstring-extraneous-exception]
    with pytest.raises(StopIteration):
        next(iter_tokens)


def check_iter_tokens_command_without_arguments(
    command: Command,
) -> None:
    context = IterTokensContext()
    items = command.iter_tokens(context)
    check_next_enter_node_token(items, type(command))
    check_next_tex_token(items, f"\\{command.name}", TexControlWordToken)
    check_next_leave_node_token(items, type(command))


def check_iter_tokens_command_with_single_string_argument(
    command: Command,
    command_cls: type[Command],
    argument: str,
) -> None:
    """Check commands that have a single argument of type `str`.

    Parameters
    ----------
    command : Command
        The command.
    command_cls : type[Command]
        The class type of the command.
    argument : str
        The argument.
    """
    context = IterTokensContext()
    items = command.iter_tokens(context)
    check_next_enter_node_token(items, command_cls)
    check_next_tex_token(items, f"\\{command.name}", TexControlWordToken)
    check_next_enter_node_token(items, Argument)
    check_next_tex_token(items, "{", TexBeginGroupToken)
    check_next_enter_node_token(items, Text)
    check_next_tex_token(items, argument, TexTextToken)
    check_next_leave_node_token(items, Text)
    check_next_tex_token(items, "}", TexEndGroupToken)
    check_next_leave_node_token(items, Argument)
    check_next_leave_node_token(items, command_cls)
    check_end_of_tokens(items)
