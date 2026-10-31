# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING

from latexcompose.base.primitive import Primitive
from latexcompose.tokens.enter_node_token import EnterNodeToken
from latexcompose.tokens.leave_node_token import LeaveNodeToken
from latexcompose.tokens.tex_text_token import TexTextToken

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.context import IterTokensContext
    from latexcompose.tokens.token import Token


def escape_latex(text: str) -> str:
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
    def __init__(self, text: str, *, linebreak: bool = False) -> None:
        r"""Insert the given text.

        If there are any characters in the text which needed to be escaped
        in LaTeX, then they get escaped.

        Parameters
        ----------
        text : str
            The text which will be added to the document
        linebreak : bool = False
            Adds a line break at the end of the text. This only
            adds `\n` to the end of the line. The character has no
            meaning in LaTeX, it just makes the generated tex document
            more readable. LaTeX has its own newline symbol, which is
            `\\` which really makes a new line the output document.
        """
        self._text = text
        self._newline = linebreak

    def iter_tokens(self, context: IterTokensContext) -> Iterator[Token]:
        yield EnterNodeToken(self)
        if self._newline:
            yield TexTextToken(escape_latex(self._text) + "\n")
        else:
            yield TexTextToken(escape_latex(self._text))
        yield LeaveNodeToken(self)
