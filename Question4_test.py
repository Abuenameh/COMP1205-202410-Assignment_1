import pytest
from unittest.mock import patch

def test_point_in_rectangle(capfd):
    # Define test cases with inputs and expected outputs
    test_cases = [
        # Inside the rectangle
        ( "(1, 1)", "Point (1, 1) is in the rectangle\n" ),
        ( "(4, 1)", "Point (4, 1) is in the rectangle\n" ),
        ( "(0, 2.5)", "Point (0, 2.5) is in the rectangle\n" ),
        
        # Outside the rectangle
        ( "(6, 1)", "Point (6, 1) is not in the rectangle\n" ),
        ( "(1, 3)", "Point (1, 3) is not in the rectangle\n" ),
        ( "(6, 3)", "Point (6, 3) is not in the rectangle\n" ),
    ]

    for point_input, expected_output in test_cases:
        with patch('builtins.input', return_value=point_input):
           with open('Question4.py') as file:
                code = file.read()
                exec(code)

        # Capture the printed output
        out, _ = capfd.readouterr()

        # Assert that the output matches the expected result
        assert out == expected_output
