# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Implements class `Writer` for writing TeX/LaTeX."""

from io import StringIO
import logging
from pathlib import Path
from typing import TYPE_CHECKING, TextIO

if TYPE_CHECKING:
    from latexcompose.base.node import Node
    from latexcompose.io.formatter import Formatter

logger = logging.getLogger(__name__)


class Writer:
    """Write a LaTeX AST to an output stream.

    The Writer is responsible for taking a root
    [Node][latexcompose.base.Node] and converting it
    into a sequence of strings using a provided
    [Formatter][latexcompose.io.Formatter]. The generated
    strings are then written to a text-based output stream.

    The Writer itself does not perform formatting or traversal logic. Instead,
    it delegates formatting to the given Formatter implementation.
    """

    def __init__(self, out: TextIO) -> None:
        """
        Parameters
        ----------
        out:
            A text stream (e.g. file or buffer) to which the generated LaTeX
            content will be written.
        """  # noqa: D205
        self._out = out

    def write(self, tex_node: Node, formatter: Formatter) -> None:
        """Write a LaTeX node to the output stream.

        The method iterates over the string representation produced by the
        formatter and writes each part to the configured output stream.

        Parameters
        ----------
        tex_node:
            Root node of the LaTeX AST to be written.
        formatter:
            Formatter responsible for converting the node into a sequence
            of strings.
        """
        for string in formatter.iter_string(tex_node):
            self._out.write(string)

    @staticmethod
    def to_file(path: Path | str, node: Node, formatter: Formatter) -> None:
        """Write a LaTeX node to a file.

        This is a convenience method that creates a Writer instance and writes
        the formatted output directly to a file.

        Parameters
        ----------
        path : Path | str
            Path to the output file.
        node : Node
            Root node of the LaTeX AST to be written.
        formatter : Formatter
            Formatter responsible for converting the node into a sequence
            of strings.
        """
        source = path if isinstance(path, Path) else Path(path)

        with source.open("w", encoding="utf-8") as f:
            writer = Writer(f)
            writer.write(node, formatter)

    @staticmethod
    def to_string(node: Node, formatter: Formatter) -> str:
        """Render a LaTeX node to a string.

        This is a convenience method that writes the formatted output to an
        in-memory buffer and returns the resulting string.

        Parameters
        ----------
        node:
            Root node of the LaTeX AST to be rendered.
        formatter:
            Formatter responsible for converting the node into a sequence
            of strings.

        Returns
        -------
        str
            The generated LaTeX code as a string.
        """
        buffer = StringIO()
        writer = Writer(buffer)
        writer.write(node, formatter)
        return buffer.getvalue()
