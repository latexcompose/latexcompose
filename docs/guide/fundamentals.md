---
icon: lucide/blocks
---

# Fundamentals

It is important to understand that `latexcompose` primarily uses
classes to build LaTeX documents.

You use these classes to __compose__ a tree-like structure.
(That is the reason why the library is called __`latexcompose`__.)

If you are looking for methods like `generate_section`,
`generate_table`, or something similar, you won't find them.
Once you say goodbye to function-based libraries and commit to
class-based document creation, you are on the right track.

In the guide we often use the expression for building "LaTeX documents",
but it is not required that you always need to create a complete LaTeX
document. Of course you also can use the classes to create only LaTeX
code snippets.

## Base classes for building LaTeX documents

### `Node`

The class [Node][latexcompose.base.Node] is the base class for
all classes that make up a LaTeX document.

There are two classes that inherit from `Node`:

- [Primitive][latexcompose.base.Primitive], which represents
  nodes that don't have any children, and
- [Container][latexcompose.base.Container], which represents
  nodes that can have children.

### `Primitive`

[Primitive][latexcompose.base.Primitive] nodes don't have any
children. Examples include:

- [Text][latexcompose.base.Text], which represents plain text
  in which special characters are escaped.
- [RawText][latexcompose.base.RawText], which represents raw text
  in which each character is printed as-is, without escaping.
  (This can be useful in rare cases, but normally you won't need
  this class.)

### `Container`

The class [Container][latexcompose.base.Container] is used for
nodes that can have children. This class gives our LaTeX documents
a tree-like structure.

A container can have child nodes, and each child node can be of
any type. This means that a child node can also have children of
its own.

There are three classes that inherit from `Container`:

- [Command][latexcompose.base.Command], which is used to define
  LaTeX commands.
- [Argument][latexcompose.base.Argument], which is used to
  represent the arguments of a command.
- [Composable][latexcompose.base.Composable], which implements
  the `compose()` method to create dynamic content at runtime.

## Token classes

After creating our LaTeX document, which can have a tree-like
structure, we need to split it into smaller pieces. These pieces
are called __tokens__. They are similar to the way LaTeX
interprets the individual parts of a document (although they are
not exactly the same, the concepts are similar).

The method [Node.iter_tokens][latexcompose.base.Node.iter_tokens]
returns a stream of tokens. It also flattens the tree-like
structure. Most of the tokens represent a string, some of them only
provide only structural information during node traversal.
