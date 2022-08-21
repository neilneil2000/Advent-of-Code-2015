from dataclasses import dataclass
from typing import Set
from day_9_input import puzzle_input

LARGE_NUMBER = 9999999999999999


@dataclass
class Segment:
    """Representation of a segment of a journey between two points"""

    Endpoints: set
    Distance: int


class RoutePlanner:
    """Route Planning Engine"""

    def __init__(self):
        self.map = {}

    def add_segment(self, segment_as_text: str):
        """Adds a segment to the planner"""
        location_a, _, location_b, _, distance = segment_as_text.split()
        distance = int(distance)

        if location_a in self.map:
            self.map[location_a][location_b] = distance
        else:
            self.map.update({location_a: {location_b: distance}})

        if location_b in self.map:
            self.map[location_b][location_a] = distance
        else:
            self.map.update({location_b: {location_a: distance}})

    def get_shortest_route(self):
        """Returns total distance of shortest route"""
        distances_by_start_location = {}
        for start_location in self.map:
            distances_by_start_location[start_location] = self._get_best_from_here(
                current_location=start_location,
                visited=set(),
                current_distance=0,
                current_best=LARGE_NUMBER,
            )

        return min(distances_by_start_location.values())

    def _get_best_from_here(
        self,
        current_location: str,
        visited: Set[str],
        current_distance: int,
        current_best: int,
    ):
        if current_distance > current_best:
            return None  # If we've already found a better route then stop

        valid_routes = dict(self.map[current_location])  # Ensure we make a copy
        for location in visited:
            valid_routes.pop(location)

        if not valid_routes:
            return current_distance  # If there's nowhere left to go then return our distance

        best_result_via_this_route = LARGE_NUMBER
        for next_location, distance in valid_routes.items():
            this_result = self._get_best_from_here(
                current_location=next_location,
                visited=visited.union({current_location}),
                current_distance=current_distance + distance,
                current_best=current_best,
            )
            if this_result < best_result_via_this_route:
                best_result_via_this_route = this_result

        return best_result_via_this_route

    def get_longest_route(self):
        """Returns total distance of longest route"""
        distances_by_start_location = {}
        for start_location in self.map:
            distances_by_start_location[start_location] = self._get_worst_from_here(
                current_location=start_location,
                visited=set(),
                current_distance=0,
                current_best=0,
            )

        return max(distances_by_start_location.values())

    def _get_worst_from_here(
        self,
        current_location: str,
        visited: Set[str],
        current_distance: int,
        current_best: int,
    ):
        valid_routes = dict(self.map[current_location])  # Ensure we make a copy
        for location in visited:
            valid_routes.pop(location)

        if not valid_routes:
            return current_distance  # If there's nowhere left to go then return our distance

        worst_result_from_here = 0
        for next_location, distance in valid_routes.items():
            this_result = self._get_worst_from_here(
                current_location=next_location,
                visited=visited.union({current_location}),
                current_distance=current_distance + distance,
                current_best=current_best,
            )
            if this_result > worst_result_from_here:
                worst_result_from_here = this_result

        return worst_result_from_here


def main():
    segments = puzzle_input.splitlines()
    santa_plan_4000 = RoutePlanner()
    for segment in segments:
        santa_plan_4000.add_segment(segment)
    shortest_distance = santa_plan_4000.get_shortest_route()
    print(shortest_distance)
    longest_distance = santa_plan_4000.get_longest_route()
    print(longest_distance)


if __name__ == "__main__":
    main()
