import pytest
from unittest.mock import patch

def test_factorial_computation(capfd):
    # Define the test inputs and expected outputs
    test_inputs = [
        (4, "The factorial is: 24\n"),     # Valid input case
        (0, "The factorial is: 1\n"),      # Edge case with zero
        (5, "The factorial is: 120\n"),    # Another valid input case
    ]
    with open("Question3.py") as file:
        code = file.read()

    for test_input, expected_output in test_inputs:
        with patch('builtins.input', return_value=test_input):
            exec(code)

        # Capture the printed output
        out, _ = capfd.readouterr()
        
        # Assert that the output matches the expected result
        assert out == expected_output
