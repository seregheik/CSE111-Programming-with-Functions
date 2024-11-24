from weather import wind_chill
from pytest import approx
import pytest

def test_wind_chill() :
    assert wind_chill(0,3) == approx(-6.9)
    assert wind_chill(-5, 5) == approx(-16.4)
    assert wind_chill(-10, 3) == approx(-18.2)

pytest.main(['-v', '--tb=no', 'test_weather.py'])