import pytest
import math
from unittest.mock import patch

def test_square_root_calculations(capfd):
    test_input = "30"
    
    with patch('builtins.input', return_value=test_input):
        import Question2
        
    out, _ = capfd.readouterr()
  
    expected_output = "1: 5.477\n2: 2.340\n3: 1.530\n"
    assert out == expected_output
