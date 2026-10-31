# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Begin`."""

from latexcompose.base import Argument, Command, Text


class Begin(Command):
    """Starts a LaTeX environment."""

    def __init__(
        self,
        environment_name: str,
    ) -> None:
        """Initialize the LaTeX environment.

        Parameters
        ----------
        environment_name : str
            Name of the LaTeX environment.
        """
        super().__init__("begin", Argument(Text(environment_name)))
