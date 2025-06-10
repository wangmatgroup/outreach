import collections

ALIVE = "♥"
DEAD = "‧"


class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern  # instance of class Pattern

    # iterations for Conway's Game of life
    def evolve(self):
        
        # relative positions of neighbors from reference cell using tuples
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        
        # defaultdict returns a dictionary 
        # in which the default value is 0 for missing keys
        # https://docs.python.org/3/library/collections.html#collections.defaultdict 
        num_neighbors = collections.defaultdict(int)
        
        # count number of neighbors for 'alive cells'
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        # create a set {...} of neighors that themselves have 2 or 3 'alive' neighbors
        # find cells that are in common with .alive_cells
        # these are the cells that stay alive between iterations
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        
        # create a set {...} of neighbors with exactly 3 'alive' neighbors
        # remove cells that are already in .alive_cells 
        # these are the cells that are revived between iterations
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        # the total set of 'alive' cells is the union of those that stay alive
        # and come alive
        self.pattern.alive_cells = stay_alive | come_alive


    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
    
    def as_string(self, bbox):
        # representation of array in terminal using bbox dimensions
        start_col, start_row, end_col, end_row = bbox
        
        # for displaying name of pattern (purely aesthetic)
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        
        # generate array of 'dead' or 'alive' cells as concatenated strings
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
            
        return "\n ".join(display)
