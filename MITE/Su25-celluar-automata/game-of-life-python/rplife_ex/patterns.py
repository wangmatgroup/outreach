from dataclasses import dataclass
from pathlib import Path

# for compatibility across different versions of Python
try:
    # compatible with Python >= 3.11
    import tomllib
except ImportError:
    import tomli as tomllib

# import the list of possible patterns
PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

# The decorator @dataclass automatically generates special methods 
# like __init__ and __repr__ to user-defined classes, which saves us effort!
# see documentation: https://docs.python.org/3/library/dataclasses.html
@dataclass
class Pattern:
    """ Array pattern in Conway's Game of Life
    
        A square array of 'dead' and 'alive' cells is tracked at each iteration.
        In this implementation, the array is initiated with 'dead' cells and 
        we keep track of the 'alive' cells only
        
    """
    
    name: str
    alive_cells: set[tuple[int, int]]
    
    #-------------

    # The decorator @classmethod is used to define a method that is 
    # bound to the class and not the instance of the class
    # In this case, it allows us to initiate the array with a pattern
    # from patterns.toml
    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )

#-------------

# general functions for getting patterns from patterns.toml
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])


def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]
