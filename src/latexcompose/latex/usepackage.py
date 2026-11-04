# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `UsePackage`."""
from enum import StrEnum

from latexcompose.base import Argument, Command, OptionGroup, Text


class PackageName(StrEnum):
    """Enumeration of LaTeX package names.

    - BABEL: Provides multilingual support and hyphenation.
    - FONTENC: Specifies font encoding.
    - GRAPHICX: Includes and manipulates graphics.
    - HYPERREF: Adds hyperlinks and PDF metadata.
    - INCONSOLATA: Provides a nice monospaced font for listings.
    - INPUTENC: Specifies input encoding.
    - LAYOUT: Displays page layout parameters.
    - LIPSUM: Generates dummy text.
    - LISTINGS: Formats source code listings.
    - LMODERN: Uses Latin Modern fonts.
    - LONGTABLE: Creates tables that span multiple pages.
    - SHOWFRAME: Shows frame for debugging page layout.
    - STANDALONE: Compiles documents to standalone images.
    - TIKZ: Creates graphics and diagrams.
    - XCOLOR: Adds color support.
    """

    BABEL = "babel"
    FONTENC = "fontenc"
    GRAPHICX = "graphicx"
    HYPERREF = "hyperref"
    INCONSOLATA = "inconsolata"
    INPUTENC = "inputenc"
    LAYOUT = "layout"
    LIPSUM = "lipsum"
    LISTINGS = "listings"
    LMODERN = "lmodern"
    LONGTABLE = "longtable"
    SHOWFRAME = "showframe"
    STANDALONE = "standalone"
    TIKZ = "tikz"
    XCOLOR = "xcolor"


class UsePackage(Command):
    r"""Generates `\usepackage[<options>]{<package_name>}`."""

    def __init__(
        self,
        package_name: str,
        options: OptionGroup | None = None,
    ) -> None:
        """Initialize command.

        Parameters
        ----------
        package_name : str
            Package name.
        options : OptionGroup | None
            Command options.
        """
        if options:
            super().__init__("usepackage", options, Argument(Text(package_name)))
        else:
            super().__init__("usepackage", Argument(Text(package_name)))
