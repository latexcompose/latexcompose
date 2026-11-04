# Copyright (c) 2026 Marco Wehnert
# SPDX-License-Identifier: MIT

from enum import StrEnum


class Unit(StrEnum):
    """Definition of units."""

    # absolute units
    PT = "pt"  # point
    PC = "pc"  # pica
    IN = "in"  # inch
    BP = "bp"  # big point
    CM = "cm"  # centimeter
    MM = "mm"  # millimeter
    DD = "dd"  # didot point
    CC = "cc"  # cicero
    SP = "sp"  # scaled point

    # relative units
    EM = "em"
    EX = "ex"

    # less common but useful
    MU = "mu"  # math unit
