---
icon: lucide/download
---
# Installation

## LaTeX

Install the complete LaTeX distribution on Ubuntu with following command:

```bash
sudo apt update
sudo apt install texlive-full
```

The size is around 8 GB. 

## Building from source

`latexcompose` can be build from the sources which you can get from
the Github repository. To be able to build the project you need to
have the following installed:

- [The package manager uv](https://docs.astral.sh/uv)
- Python 3.14 or higher

## Download the repository

1. Check out the code from the
   [latexcompose repository](https://github.com/latexcompose/latexcompose)
   ```
   git clone https://github.com/latexcompose/latexcompose.git
   ```

2. Run `uv sync` in the project directory to download and install the
   dependencies in the project's virtual environment.

3. After that there are several possibilities:
    - Use `uv run` to run a script
    - Build the distribution
    - Activate the virtual environment and run python
    - Run python command from virtual environment

## Run scripts using `uv run`

You can run a script from the examples. The examples are located
in folder `docs/code/examples`. From the project root run

```py
uv run python docs/code/examples/hello_world.py
```