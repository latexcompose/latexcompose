# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

"""Contains class `Composable`."""

from typing import TYPE_CHECKING, final, override

from .container import Container

if TYPE_CHECKING:
    from collections.abc import Iterable

    from .node import Node


class Composable(Container):
    """Extend the base class with the method `compose()`.

    The class can be used as base class for any class which will
    create the content by overwriting the method `compose()`.

    ```python
    class Composable:
        def compose(self) -> Iterable[Node]:
            yield Text("latexcompose is awesome!")
    ```
    """

    def compose(self) -> Iterable[Node]:  # ruff: ignore[no-self-use]
        """Compose dynamic content.

        Returns
        -------
        Iterable[Node]
            Yields content at runtime.
        """
        return iter([])

    @final
    @override
    def _compose_children(self) -> list[Node]:
        """Return additional children created by method `compose`.

        The method is declared as final, because child classes shall
        override the method `compose`.

        Returns
        -------
        list[Node]
            Additional child nodes to be added to the container.
        """
        return list(self.compose())
