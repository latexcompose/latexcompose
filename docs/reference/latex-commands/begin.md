# `\begin`

Starts a LaTeX environment. Every environment must be closed
with the corresponding `\end` command.

## LaTeX syntax
```latex
\begin{<environment_name>}
...
\end{<environment_name>}
```

For further information see
[https://latexref.xyz/Environments.html](https://latexref.xyz/Environments.html){:target="_blank" rel="noopener noreferrer"}

See also: [`\end`](end.md)

## Python example
```python
Begin("center")
Text("latexcompose is awesome!")
End("center")
```

## Generated LaTeX code

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