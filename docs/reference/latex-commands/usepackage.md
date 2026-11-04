# `\usepackage`

Imports a LaTeX package.

## LaTeX syntax
```latex
\usepackage[<options>]{<package_name>}
```

For further information see
[](https://latexref.xyz/_005cusepackage.html)

## Python example
```python
UsePackage(PackageName.XCOLOR)
UsePackage(PackageName.FONTENC, OptionGroup(Option("T1")))
```

## Generated LaTeX code

```latex
\usepackage{xcolor}
\usepackage[T1]{fontenc}
```

## API reference

::: latexcompose.latex.UsePackage
    options:
      filters:
        - "!^_"
        - "^__init__$"