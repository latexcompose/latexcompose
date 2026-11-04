# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from enum import StrEnum

from latexcompose.base import Argument, Command, OptionGroup, Text


class DocumentClassName(StrEnum):
    """Enum for some document classes."""

    ARTICLE = "article"
    BEAMER = "beamer"
    BOOK = "book"
    LETTER = "letter"
    LETTER2E = "letter2e"
    REPORT = "report"
    SCRARTCL = "scrartcl"  # KOMA-Script article class
    SCRLTTR2 = "scrlttr2"
    STANDALONE = "standalone"


class DocumentClass(Command):
    r"""Generates LaTeX command `\documentclass[<options>]{<document_class>}`."""  # ruff: ignore[line-too-long]

    def __init__(
        self,
        document_class: str,
        options: OptionGroup | None = None,
    ) -> None:
        if options:
            super().__init__("documentclass",
                              options,
                              Argument(Text(document_class)))
        else:
            super().__init__("documentclass", Argument(Text(document_class)))
