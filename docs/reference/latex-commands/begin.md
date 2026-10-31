# `\begin`

Starts a LaTeX environment. Every environment must be closed
with the corresponding `\end` command.

## LaTeX syntax
```latex
\begin{<environment_name>}
...
\end{<environment_name>}
```

For further information, see the
[LaTeX reference on environments](https://latexref.xyz/Environments.html)

See also: [`\end`](end.md)

## Python example
```python
Begin("center")
Text("latexcompose is awesome!")
End("center")
```

## Generated LaTeX

```latex
\begin{center}
latexcompose is awesome!
\end{center}
```

## API reference 

::: latexcompose.latex.Begin
    options:
      filters:
        - "!^_"
        - "^__init__$"