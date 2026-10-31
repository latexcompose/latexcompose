# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from latexcompose.base import Argument, Command, Node


class Textbf(Command):
    r"""Represents the LaTeX command `\textbf`."""

    def __init__(self, *content: Node) -> None:
        """Initialize a bold text command.

        Parameters
        ----------
        *content : Node
            Nodes representing the content to be enclosed in the bold text
            command. If a single Argument is provided, it is used directly.
            Otherwise, all nodes are wrapped in a single Argument.
        """
        argument = (
            content[0]
            if len(content) == 1 and isinstance(content[0], Argument)
            else Argument(*content)
        )

        super().__init__("textbf", argument)
