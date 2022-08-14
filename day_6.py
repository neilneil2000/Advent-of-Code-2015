"""Advent of Code 2015 Day 6"""
from day_6_input import day_6_input

from collections import namedtuple
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple

Point = namedtuple("Point", ("x", "y"))


class CommandAction(Enum):
    on = auto()
    off = auto()
    toggle = auto()


@dataclass
class LightCommand:
    """Representation of a Command for LightGrid"""
    start_point: Point
    end_point: Point
    action: CommandAction = None


class LightGrid:
    """Representation of a Grid of Lights"""

    def __init__(self, size: Tuple[int, int]):
        self.x, self.y = size
        self.lights_on = set()

    def switch_on_light(self, light_position:Point):
        """Switch on light at position light_position"""
        self.lights_on.add(light_position)

    def switch_off_light(self, light_position:Point):
        """Switch off light at position light_position"""
        self.lights_on.discard(light_position)

    def toggle_light(self, light_position:Point):
        """Toggle light at position light_position"""
        if light_position in self.lights_on:
            self.switch_off_light(light_position)
        else:
            self.switch_on_light(light_position)

    @property
    def number_of_lights_on(self):
        """Return number of lights currently on"""
        return len(self.lights_on)




class LightController:
    """Controller that can interpret commands and co-ordinate LightGrids"""

    def execute_command(self, command: str, grid: LightGrid):
        """Implement Command on Grid"""
        command = self._parse_command(command)
        self._do_action(command,grid)

    @staticmethod
    def _parse_command(command: str):
        """Translate Human Readable to Computer Readable Command"""
        # turn off 301,3 through 808,453
        # turn on 351,678 through 951,908
        # toggle 720,196 through 897,994
        command_words = command.split()
        if command_words[0] == "turn":
            command_words.pop(0)
        x, y = command_words[1].split(",")
        start = Point(int(x), int(y))
        x, y = command_words[3].split(",")
        end = Point(int(x), int(y))

        light_command = LightCommand(start,end)

        match command_words[0]:
            case "toggle":
                light_command.action=CommandAction.toggle
            case "on":
                light_command.action=CommandAction.on
            case "off":
                light_command.action=CommandAction.off

        return light_command

    @staticmethod
    def _do_action(command: LightCommand,grid:LightGrid):
        x_parameters = [command.start_point.x,command.end_point.x]
        x_parameters.sort()
        y_parameters = [command.start_point.y,command.end_point.y]
        y_parameters.sort()

        for x in range(x_parameters[0],x_parameters[1]+1):
            for y in range(y_parameters[0],y_parameters[1]+1):
                match command.action:
                    case CommandAction.on:
                        grid.switch_on_light(Point(x,y))
                    case CommandAction.off:
                        grid.switch_off_light(Point(x,y))
                    case CommandAction.toggle:
                        grid.toggle_light(Point(x,y))


        
        
        


def main():
    """Main Function"""
    my_lights = LightGrid((1000, 1000))
    my_light_controller = LightController()
    commands = day_6_input.splitlines()
    for command in commands:
        my_light_controller.execute_command(command, my_lights)
    print(f"{my_lights.number_of_lights_on} lights on at end of sequence")


if __name__ == "__main__":
    main()
