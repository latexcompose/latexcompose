---
icon: simple/python
---

# Examples

The folder `docs/code/examples` contains several examples that
demonstrate how to build LaTeX documents using `latexcompose`.
Let's start with a simple example: `hello_world.py`.

The following sections walk through the implementation step by
step.

<!--
Keep this as an example of how to create a collapsible admonition
with tabs.

???+ example "hello_world.py"

    ===+ "Compose document"

        ```python linenums="14"
        --8<-- "docs/code/examples/hello_world.py:compose"
        ```

    === "Full code"

        ```python linenums="1"
        --8<-- "docs/code/examples/hello_world.py"
        ```
-->

## Defining the document

Let's first look at the implementation of the `HelloWorld` class:

```python linenums="12"
--8<-- "docs/code/examples/hello_world.py:12:20"
```

The class inherits from `Composable` and implements its `compose()`
method. This method defines the structure of our LaTeX document by
yielding a sequence of nodes.

We start by creating an instance of
[DocumentClass][latexcompose.latex.DocumentClass], specifying
`article` as the document class. Next, we use
[Begin][latexcompose.latex.Begin] to start the `document` environment.

The actual document content is represented by a `Text` node
containing the text `Hello world!`. Finally,
[End][latexcompose.latex.End] closes the document environment.

Notice that we don't write any LaTeX commands directly. Instead, we
describe the document structure using Python objects.
`latexcompose` takes care of converting these objects into their
corresponding LaTeX representation.

## Generating the LaTeX file
Defining the document structure is only the first step. We also need
to generate the actual `.tex` file.

This is done by the `generate_hello_world()` function:

```python linenums="21"
--8<-- "docs/code/examples/hello_world.py:21:29"
```

First, we instantiate our `HelloWorld` class. We then pass this
instance to `Writer.to_file()`, which writes the resulting LaTeX
document to a file.

The output path is constructed using
`Path(__file__).with_suffix(".tex")`. This ensures that the
generated file is placed next to the Python source file, using the
same filename but with the `.tex` extension.

We also provide a `PrettyFormatter` with an `IterTokensContext`.
The formatter is responsible for formatting the generated LaTeX
output, while the context provides the information needed during
token iteration.

## Generated LaTeX

Running `hello_world.py` generates the following LaTeX document:

```latex linenums="1"
--8<-- "docs/code/examples/hello_world.tex"
```

As you can see, the resulting LaTeX document contains the document
class declaration, the document environment and our `Hello world!`
text.

The important point is that we defined the entire document using
Python objects. `latexcompose` translated this structure into valid
LaTeX code and wrote it to a file.

You can find the [complete example here](examples/hello_world.md).