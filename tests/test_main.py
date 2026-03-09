import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5   # FAILS: add() returns 2-3 = -1, not 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0