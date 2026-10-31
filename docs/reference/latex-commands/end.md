# `\end`

Ends a LaTeX environment.

## LaTeX syntax
```latex
\begin{<environment_name>}
...
\end{<environment_name>}
```

For further information, see the
[LaTeX reference on environments](https://latexref.xyz/Environments.html)

See also: [`\begin`](begin.md)

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

::: latexcompose.latex.End
    options:
      filters:
        - "!^_"
        - "^__init__$"