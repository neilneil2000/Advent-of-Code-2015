from enum import Enum
from typing import List, Tuple


def read_input(filename: str):
    """Read Light Grid Input File"""
    with open(filename, "r", encoding="utf-8") as filehandle:
        file_data = [list(line.strip()) for line in filehandle]
    return file_data


class LightStatus(Enum):
    """Enumeration of Light Status"""

    ON = "#"
    OFF = "."


class LightGrid:
    """Representation of a Light Grid"""

    def __init__(self, light_status: List) -> None:
        self.light_status = light_status

    @property
    def grid_length(self) -> int:
        """Number of rows in grid"""
        return len(self.light_status)

    @property
    def grid_width(self) -> int:
        """Number of columns in grid"""
        return len(self.light_status[0])

    def _get_neighbours(self, location: Tuple[int, int]) -> List:
        """Return list of valid neighbours"""
        x, y = location
        neighbours = {
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        }

        for neighbour in neighbours.copy():
            x, y = neighbour
            if 0 <= x < self.grid_width and 0 <= y < self.grid_length:
                continue
            neighbours.discard(neighbour)

        return neighbours

    def _get_light_status(self, location: Tuple[int, int]) -> LightStatus:
        x, y = location
        status = self.light_status[y][x]
        if status is LightStatus.ON.value:
            return LightStatus.ON
        return LightStatus.OFF.value

    def _get_neighbours_that_are_on(self, location: Tuple[int, int]) -> int:
        number_on = 0
        for neighbour in self._get_neighbours(location):
            if self._get_light_status(neighbour) is LightStatus.ON:
                number_on += 1
        return number_on

    def execute_steps(self, number_of_steps: int) -> None:
        """Execute number of steps"""
        for _ in range(number_of_steps):
            self.set_corners_on()
            self._execute_one_step()
        self.set_corners_on()

    def _get_new_value(self, location) -> str:
        x, y = location
        neighbours_on = self._get_neighbours_that_are_on(location)
        if self.light_status[y][x] is LightStatus.ON.value and 2 <= neighbours_on <= 3:
            return LightStatus.ON.value
        if self.light_status[y][x] is LightStatus.OFF.value and neighbours_on == 3:
            return LightStatus.ON.value
        return LightStatus.OFF.value

    def _execute_one_step(self) -> None:
        new_grid = [["."] * self.grid_width for _ in range(self.grid_length)]
        for row in range(self.grid_length):
            for column in range(self.grid_width):
                new_grid[row][column] = self._get_new_value((column, row))
        self.light_status = new_grid

    def set_corners_on(self) -> None:
        corners = [
            (0, 0),
            (0, self.grid_length - 1),
            (self.grid_width - 1, 0),
            (self.grid_width - 1, self.grid_length - 1),
        ]

        for corner in corners:
            x, y = corner
            self.light_status[y][x] = LightStatus.ON.value

    def print_light_grid(self) -> None:
        for row in self.light_status:
            print("".join(row))

    @property
    def number_of_lights_on(self) -> int:
        """Return number of lights on"""
        lights_on = 0
        for row in self.light_status:
            lights_on += row.count(LightStatus.ON.value)
        return lights_on


def main():
    """Main Solution"""
    initial_light_status = read_input("day_18_input.txt")
    my_lights = LightGrid(initial_light_status)
    my_lights.execute_steps(100)
    print(my_lights.number_of_lights_on)


if __name__ == "__main__":
    main()
