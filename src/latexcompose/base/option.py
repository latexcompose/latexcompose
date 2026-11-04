# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Self, override

from latexcompose.base.composable import Composable
from latexcompose.base.group_delimiter import GroupDelimiter
from latexcompose.base.node import Node
from latexcompose.tokens import (
    EnterNodeToken,
    LeaveNodeToken,
    TexBeginGroupToken,
    TexBeginOptionGroupToken,
    TexEndGroupToken,
    TexEndOptionGroupToken,
    TexTextToken,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.context import IterTokensContext
    from latexcompose.tokens.token import Token


class Option(Composable):
    """A single key-value option.

    An option consists of a key and an optional value. The value can be
    a string, an integer, a LaTeX node, or another option.

    When multiple options are supplied as the value, they are grouped
    using curly braces. This allows nested option structures, as commonly
    used by TikZ and pgfkeys.

    Parameters
    ----------
    key : str
        The option key.
    *values : str | int | Node | Option
        The optional value of the option.

        The following forms are supported:

        - No values: creates a key without a value.
        - One string or integer: creates a simple key-value pair.
        - One node: uses the node as the value.
        - One option: creates a nested option group using curly braces.
        - Multiple options: creates a nested option group using curly
          braces. All supplied values must be options.

    Raises
    ------
    TypeError
        If multiple values are supplied and any of them is not an
        ``Option`` instance.

    Examples
    --------
    A simple option without a value:

    >>> Option("draw")

    A key-value option:

    >>> Option("color", "red")

    A nested option group:

    >>> Option("style", Option("draw"), Option("thick"))
    """

    def __init__(
        self,
        key: str,
        *values: str | int | Node | Option,
    ) -> None:
        self._key = key
        self._value: str | int | Node | None = None

        if not values:
            super().__init__()
            return

        if len(values) == 1:
            value = values[0]

            if isinstance(value, Option):
                self._value = OptionGroup(
                    value,
                    delimiter=GroupDelimiter.BRACES,
                )
            elif isinstance(value, (str, int, Node)):
                self._value = value
            else:
                msg = f"Unsupported value type: {type(value).__name__}"
                raise TypeError(msg)

        else:
            if not all(isinstance(value, Option) for value in values):
                msg = (
                    f"Multiple values for option '{key}' must all be "
                    "Option instances."
                )
                raise TypeError(msg)

            options = [value for value in values if isinstance(value, Option)]

            self._value = OptionGroup(
                *options,
                delimiter=GroupDelimiter.BRACES,
            )

        if isinstance(self._value, Node):
            super().__init__(self._value)
        else:
            super().__init__()

    @property
    def key(self) -> str:
        """The option key."""
        return self._key

    @property
    def value(self) -> str | int | Node | None:
        """The option value, or ``None`` if the option has no value."""
        return self._value

    @override
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterator[Token]:
        """Generate the tokens representing this option.

        Parameters
        ----------
        context : IterTokensContext
            The token generation context.

        Yields
        ------
        Token
            Tokens representing the option key and its optional value.
        """
        yield EnterNodeToken(self)
        yield TexTextToken(self._key)

        if self._value is not None:
            yield TexTextToken("=")

            if isinstance(self._value, str):
                yield TexTextToken(self._value)
            elif isinstance(self._value, int):
                yield TexTextToken(str(self._value))
            else:
                yield from self._value.iter_tokens(context=context)

        yield LeaveNodeToken(self)


class OptionGroup(Composable):
    """A comma-separated group of options.

    An option group contains zero or more ``Option`` instances. The
    options are separated by commas and enclosed by a configurable pair
    of delimiters.

    By default, an option group uses square brackets. This is useful
    for representing optional arguments in LaTeX commands.

    Curly braces can be used for nested option groups, for example
    when an option itself contains multiple options.

    Parameters
    ----------
    *options : Option
        The options contained in the group.
    delimiter : GroupDelimiter, default=GroupDelimiter.BRACKETS
        The delimiters enclosing the group.

    Raises
    ------
    TypeError
        If any supplied child is not an ``Option`` instance.

    Examples
    --------
    A group of options:

    >>> OptionGroup(Option("draw"), Option("thick"))

    A group using curly braces:

    >>> OptionGroup(
    ...     Option("draw"),
    ...     Option("thick"),
    ...     delimiter=GroupDelimiter.BRACES,
    ... )

    An empty group produces no tokens.
    """

    def __init__(
        self,
        *options: Option,
        delimiter: GroupDelimiter = GroupDelimiter.BRACKETS,
    ) -> None:
        if not all(isinstance(option, Option) for option in options):
            msg = "All children of an OptionGroup must be Option instances."
            raise TypeError(msg)

        super().__init__(*options)
        self._delimiter = delimiter

    @property
    def delimiter(self) -> GroupDelimiter:
        """The delimiters enclosing this group."""
        return self._delimiter

    def set_option(self, option: Option) -> Self:
        """Add an option or replace an existing option with the same key.

        If an option with the same key already exists, it is replaced
        in its current position. Otherwise, the new option is appended.

        Parameters
        ----------
        option : Option
            The option to add or replace.

        Returns
        -------
        Self
            This option group, allowing method chaining.

        Raises
        ------
        TypeError
            If the supplied value is not an ``Option`` instance.
        """
        if not isinstance(option, Option):
            msg = "Expected an Option instance."
            raise TypeError(msg)

        for index, existing in enumerate(self._children):
            if isinstance(existing, Option) and existing.key == option.key:
                self._children[index] = option
                return self

        self._children.append(option)
        return self

    def extend(self, other: OptionGroup) -> Self:
        """Append all options from another option group.

        Existing options are not replaced, even if they have the same
        key. Use :meth:`set_option` when replacement behavior is
        required.

        Parameters
        ----------
        other : OptionGroup
            The option group whose options are appended.

        Returns
        -------
        Self
            This option group, allowing method chaining.

        Raises
        ------
        TypeError
            If the supplied value is not an ``OptionGroup`` instance.
        """
        if not isinstance(other, OptionGroup):
            msg = "Expected an OptionGroup instance."
            raise TypeError(msg)

        self._children.extend(other._children)
        return self

    @override
    def iter_tokens(
        self,
        context: IterTokensContext,
    ) -> Iterator[Token]:
        """Generate the tokens representing this option group.

        The options are separated by commas and enclosed by the
        configured delimiters. An empty group produces no tokens.

        Parameters
        ----------
        context : IterTokensContext
            The token generation context.

        Yields
        ------
        Token
            Tokens representing the delimited option group.
        """
        self._mount()

        if not self._children:
            return

        yield EnterNodeToken(self)

        if self._delimiter is GroupDelimiter.BRACES:
            yield TexBeginGroupToken()
        else:
            yield TexBeginOptionGroupToken()

        for index, option in enumerate(self._children):
            if index > 0:
                yield TexTextToken(",")

            yield from option.iter_tokens(context=context)

        if self._delimiter is GroupDelimiter.BRACES:
            yield TexEndGroupToken()
        else:
            yield TexEndOptionGroupToken()

        yield LeaveNodeToken(self)

    def __len__(self) -> int:
        """Return the number of options in this group.

        Returns
        -------
        int
            The number of options.
        """
        return len(self._children)
