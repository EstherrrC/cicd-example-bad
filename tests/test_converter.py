import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius
import pytest

def test_celsius_to_fahrenheit():
    # This test WILL FAIL because the formula in converter.py is wrong
    assert celsius_to_fahrenheit(0) == 32      # returns 0, not 32 ← FAIL
    assert celsius_to_fahrenheit(100) == 212   # returns 180, not 212 ← FAIL

def test_fahrenheit_to_celsius():
    # This test passes
    assert round(fahrenheit_to_celsius(32), 2) == 0.0
    assert round(fahrenheit_to_celsius(212), 2) == 100.0