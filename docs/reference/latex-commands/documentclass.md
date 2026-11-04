# `\documentclass`

Defines the document class. The command is usually the first command
in a LaTeX document.

## LaTeX syntax
```latex
\documentclass[<options>]{<class>}
```

For further information see
[https://latexref.xyz/Document-classes.html](https://latexref.xyz/Document-classes.html){:target="_blank" rel="noopener noreferrer"}

## Python example

!!! warning "Important"

    The order of arguments in Python differs from the
    corresponding LaTeX command because optional arguments must
    be defined after the mandatory commands. Make sure to use the
    Python argument order.

```python
DocumentClass("article")
DocumentClass("standalone", OptionGroup(Option("a4paper")))
```

## Generated LaTeX code

```latex
\documentclass{article}
\documentclass[a4paper]{article}
```