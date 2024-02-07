# Inside test_main.py

import sys
import os

# Add the parent directory to sys.path to allow importing from the parent directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now you can import my_function from main.py
from main import my_function


def test_my_function():
    # Test with integers
    assert my_function(2, 3) == 6
    # Test with floats
    assert my_function(2.5, 3.5) == 6.0
    # Test with negative numbers
    assert my_function(-2, -3) == -5
