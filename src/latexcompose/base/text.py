# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains the `Text` class and LaTeX text escaping utilities."""

from typing import TYPE_CHECKING

from latexcompose.base.primitive import Primitive
from latexcompose.tokens.enter_node_token import EnterNodeToken
from latexcompose.tokens.leave_node_token import LeaveNodeToken
from latexcompose.tokens.tex_newline_token import TexNewlineToken
from latexcompose.tokens.tex_text_token import TexTextToken

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.context import IterTokensContext
    from latexcompose.tokens.token import Token


def escape_latex(text: str) -> str:
    r"""Escape special characters in ordinary LaTeX text.

    Parameters
    ----------
    text : str
        Text to escape.

    Returns
    -------
    str
        Text with LaTeX special characters escaped.
    """
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
    }

    for char, replacement in replacements.items():
        text = text.replace(char, replacement)

    return text


class Text(Primitive):
    """Represent ordinary text in a LaTeX document."""

    def __init__(self, text: str, *, linebreak: bool = False) -> None:
        r"""Initialize a text node.

        The supplied text is automatically escaped to ensure that
        LaTeX special characters are treated as ordinary text.

        Parameters
        ----------
        text : str
            Text to insert into the document.
        linebreak : bool, default=False
            Whether to add a source-code line break after the text.
            This only affects the generated LaTeX source code and
            does not create a line break in the rendered document.
            For an actual LaTeX line break, use ``\\``.
        """
        self._text = text
        self._linebreak = linebreak

    def iter_tokens(self, context: IterTokensContext) -> Iterator[Token]:
        """Generate tokens representing this text node.

        Parameters
        ----------
        context : IterTokensContext
            Context used during token generation.

        Yields
        ------
        Token
            Tokens representing the text and its optional source-code
            line break.
        """
        yield EnterNodeToken(self)
        yield TexTextToken(escape_latex(self._text))

        if self._linebreak:
            yield TexNewlineToken()

        yield LeaveNodeToken(self)
