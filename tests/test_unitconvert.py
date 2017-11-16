import numpy as np
import pytest
from unitconvert import distance, temperature

def test_temperature():

    tempf = 32
    assert temperature.fahrenheit_to_celsius(tempf)==0

    tempc = 0
    assert temperature.celsius_to_fahrenheit(tempc)==32

def test_distance():

    distm = 1
    assert distance.miles_to_kilometers(distm) == 1.61

    distk = 1.61
    assert distance.kilometers_to_miles(distk) == 1
