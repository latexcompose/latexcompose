# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains classes IterTokensContext and IterTreeContext."""


class IterTokensContext:
    """Context for the method [Node.iter_tokens][latexcompose.base.node.Node.iter_tokens]."""

    def __init__(self) -> None:
        """Initialize instance attributes."""
        self.section_level: int = 0
        """The current section level. In LaTeX there are the commands
        for section, subsection and so on. In latexcompose library there is
        only one class `Section` which can be nested. Therefore we need
        to keep track in which section are we at the moment to be able
        to generate the correct section command."""


class IterTreeContext:
    """Context for the method `Node.iter_tree`.

    The class does not have any attributes, but it will be used for
    method `Node.iter_tree` to pass a context to the childs. It's
    better to pass the context now, because later it would be painful
    to refactor all methods. You can create a child class and implement
    additional features.
    """
