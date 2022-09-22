from day_18 import LightGrid, LightStatus
import pytest

"""([initial light status,number of neighbours on],expected light status)"""
test_parameters = [
    ([LightStatus.ON, 0], LightStatus.OFF),
    ([LightStatus.ON, 1], LightStatus.OFF),
    ([LightStatus.ON, 2], LightStatus.ON),
    ([LightStatus.ON, 3], LightStatus.ON),
    ([LightStatus.ON, 4], LightStatus.OFF),
    ([LightStatus.ON, 5], LightStatus.OFF),
    ([LightStatus.ON, 6], LightStatus.OFF),
    ([LightStatus.ON, 7], LightStatus.OFF),
    ([LightStatus.ON, 8], LightStatus.OFF),
    ([LightStatus.OFF, 0], LightStatus.OFF),
    ([LightStatus.OFF, 1], LightStatus.OFF),
    ([LightStatus.OFF, 2], LightStatus.OFF),
    ([LightStatus.OFF, 3], LightStatus.ON),
    ([LightStatus.OFF, 4], LightStatus.OFF),
    ([LightStatus.OFF, 5], LightStatus.OFF),
    ([LightStatus.OFF, 6], LightStatus.OFF),
    ([LightStatus.OFF, 7], LightStatus.OFF),
    ([LightStatus.OFF, 8], LightStatus.OFF),
]


@pytest.mark.parametrize("test_input,expected_output", test_parameters)
def test_get_new_value(test_input, expected_output, mocker):
    """Test for LightStatus._get_new_value"""
    initial_light_status, neighbours = test_input
    test_grid = LightGrid([[initial_light_status.value]])
    mocker.patch(
        "day_18.LightGrid._get_neighbours_that_are_on", return_value=neighbours
    )
    output = test_grid._get_new_value((0, 0))

    assert output == expected_output.value
