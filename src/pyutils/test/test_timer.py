import pytest
from pyutils import timer

@timer(num_times = 5)
def waste_time(n):
    for i in range(n):
        pass

def test_timer_returns_float():
    assert isinstance(waste_time(100), float)

def test_timer_prints_correctly(capfd):
    waste_time(1)
    # capfd is a fixture provided by pytest, see:
    # https://stackoverflow.com/questions/20507601/writing-a-pytest-function-for-checking-the-output-on-console-stdout

    out, err = capfd.readouterr()
    assert out == "Average run time of 'waste_time': 0.0000 s\n"

def test_timer_catches_type_error():
    with pytest.raises(TypeError):
        waste_time("100")
