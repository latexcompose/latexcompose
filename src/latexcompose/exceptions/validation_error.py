# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

class ValidationError(Exception):
    """Raised when validation of nodes failed."""

    def __init__(self, message: str) -> None:
        """Initialize with error message.

        Parameters
        ----------
        message : str
            Error message
        """
        super().__init__(message)
