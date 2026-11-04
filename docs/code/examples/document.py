from pathlib import Path
from typing import TYPE_CHECKING

from latexcompose.base import (
    Composable,
    IterTokensContext,
    Node,
    Option,
    OptionGroup,
    Text,
)
from latexcompose.io import PrettyFormatter, Writer
from latexcompose.latex import UsePackage, PackageName, Textbf
from latexcompose.latex.begin import Begin
from latexcompose.latex.documentclass import DocumentClass
from latexcompose.latex.end import End

if TYPE_CHECKING:
    from collections.abc import Iterator


class HelloWorld(Composable):

    def compose(self) -> Iterator[Node]:
        yield DocumentClass("article", OptionGroup(Option("a4paper")))
        yield UsePackage(PackageName.FONTENC, OptionGroup(Option("T1")))
        yield UsePackage(PackageName.XCOLOR)
        yield Begin("document")
        yield Textbf(Text("latexcompose"))
        yield Text("is awesome!")
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
