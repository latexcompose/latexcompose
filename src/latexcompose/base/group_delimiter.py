# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `GroupDelimiter`."""

from enum import Enum


class GroupDelimiter(Enum):
    """Supported delimiters for LaTeX arguments."""

    BRACES = "{}"
    BRACKETS = "[]"
