from dataclasses import dataclass

UNFLAGGED = 0
FLAGGED = 1


@dataclass
class MineSweeper:  # type: ignore
    board: list

    def get_flagged_cells(self):
        flagged_cells = []
        for cell in self.board:
            if cell[1] == FLAGGED:
                flagged_cells.append(cell)
        return flagged_cells


if __name__ == "__main__":
    thing = MineSweeper([(i, UNFLAGGED, UNFLAGGED) for i in range(64)])
    thing.board[2] = (2, FLAGGED, 0)

    assert thing.get_flagged_cells() == [(2, 1, 0)]
    print(thing.get_flagged_cells())
