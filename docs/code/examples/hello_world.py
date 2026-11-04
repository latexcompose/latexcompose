from pathlib import Path
from typing import TYPE_CHECKING

from latexcompose.base import Composable, IterTokensContext, Node, Text
from latexcompose.io import PrettyFormatter, Writer
from latexcompose.latex.begin import Begin
from latexcompose.latex.documentclass import DocumentClass
from latexcompose.latex.end import End

if TYPE_CHECKING:
    from collections.abc import Iterable

class HelloWorld(Composable):

    def compose(self) -> Iterable[Node]:
        yield DocumentClass("article")
        yield Begin("document")
        yield Text("Hello world!")
        yield End("document")


def generate_hello_world() -> None:
    document = HelloWorld()
    Writer.to_file(
        Path(__file__).with_suffix(".tex"),
        document,
        PrettyFormatter(IterTokensContext()),
    )


if __name__ == "__main__":
    generate_hello_world()
