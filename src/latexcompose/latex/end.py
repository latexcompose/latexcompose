from latexcompose.base import Argument, Command, Text


class End(Command):

    def __init__(
        self,
        environment_name: str,
    ) -> None:
        super().__init__("end", Argument(Text(environment_name)))