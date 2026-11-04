# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
from typing import TYPE_CHECKING

from latexcompose.latex import UsePackage
from latexcompose.latex.begin import Begin
from latexcompose.latex.documentclass import DocumentClass
from latexcompose.latex.end import End
from latexcompose.tokens import (
    EnterNodeToken,
    LeaveNodeToken,
    TexControlToken,
    TexToken,
    Token,
)

# Import your actual TikZ base class here.
# from latexcompose.packages.tikz.tikz_element import TikzElement

if TYPE_CHECKING:
    from collections.abc import Iterator

    from latexcompose.base.context import IterTokensContext
    from latexcompose.base.node import Node

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class FormattingRule:
    """Formatting rules for a node type."""

    before: str = ""
    after: str = ""


class Formatter(ABC):
    """Interface for formatting a node to a LaTeX string."""

    @abstractmethod
    def iter_string(self, node: Node) -> Iterator[str]:
        """Iterate through the node and yield strings."""


class PrettyFormatter(Formatter):
    """Formats LaTeX nodes with readable whitespace."""

    def __init__(
        self,
        context: IterTokensContext,
    ) -> None:
        self._context = context

        # Formatting rules are matched using isinstance().
        self._formatting_rules: dict[type[Node], FormattingRule] = {
            DocumentClass: FormattingRule(after="\n"),
            UsePackage: FormattingRule(after="\n"),
            Begin: FormattingRule(after="\n"),
            End: FormattingRule(before="\n", after="\n"),
            #Section: FormattingRule(before="\n\n", after="\n\n"),
            #TikzElement: FormattingRule(after="\n"),
        }

    def _get_formatting_rule(
        self,
        node: Node,
    ) -> FormattingRule:
        """Return the formatting rule matching a node."""

        for node_type, rule in self._formatting_rules.items():
            if isinstance(node, node_type):
                return rule

        return FormattingRule()

    def iter_string(
        self,
        node: Node,
    ) -> Iterator[str]:
        """Generate a formatted LaTeX string."""

        last_tex_token: Token | None = None
        stack: list[Node] = []

        for token in node.iter_tokens(self._context):

            if isinstance(token, TexToken):
                current_string = str(token)

                logger.debug(
                    'Handle token type "%s", string = %s',
                    token.__class__.__name__,
                    current_string,
                )

                # A control word followed by another letter needs a
                # delimiter. Otherwise, LaTeX would interpret both as
                # one control word.
                if (
                    isinstance(last_tex_token, TexControlToken)
                    and current_string
                    and current_string[0].isalpha()
                ):
                    yield "{}"

                yield current_string

                last_tex_token = token

            elif isinstance(token, EnterNodeToken):
                stack.append(token.node)

                rule = self._get_formatting_rule(token.node)

                if rule.before:
                    yield rule.before

            elif isinstance(token, LeaveNodeToken):
                rule = self._get_formatting_rule(token.node)

                if rule.after:
                    yield rule.after

                stack.pop()