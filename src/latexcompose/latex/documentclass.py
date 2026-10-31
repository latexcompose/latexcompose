# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from latexcompose.base import Command, Argument, Text

class DocumentClass(Command):

    def __init__(
        self,
        document_class: str,
    ) -> None:
        super().__init__("documentclass", Argument(Text(document_class)))
