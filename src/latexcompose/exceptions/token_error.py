# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT


class TokenInitializationError(Exception):
    """Raised when token gets initialized with invalid values.

    This is used for example to check if a `TexControlToken` gets
    initialized with text that shall be a valid control word or
    control symbol.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
