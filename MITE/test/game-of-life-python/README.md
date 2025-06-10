# `rplife` and Conway's Game of Life

Conway's Game of Life in your terminal, to accompany the Real Python tutorial [Build Conway's Game of Life With Python](https://realpython.com/conway-game-of-life-python/).

## Navigating folders

There are three folders in this directory.

Requires running in Python 
- rplife_ex: Game of Life in your terminal with missing code for in lab exercises
- rplife: Game of life in your terminal with missing code filled in 

Run directly in the terminal as an application
- rplife_cli: Game of life in your terminal with command line interface (cli)

## Installation with cli

1. Create and activate a Python virtual environment:

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install `rplife` in editable mode:

```sh
(venv) $ cd rplife_cli
(venv) $ pip install -e .
```

## Execution

To execute `rplife`, go ahead and run the following command:

```sh
(venv) $ rplife -a
```

## Author

Real Python - Email: office@realpython.com
Modifications - Email: wwwennie@che.utexas.edu

## License

Distributed under the MIT license. See `LICENSE` for more information.
