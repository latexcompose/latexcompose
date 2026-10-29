# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""latexcompose - Library for LaTeX"""

from importlib.metadata import PackageNotFoundError, version

try:  # ruff: ignore[non-empty-init-module]
    __version__ = version("latexcompose")
except PackageNotFoundError:
    __version__ = "0.0.0"
