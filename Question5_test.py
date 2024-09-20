import pytest
from unittest.mock import patch
import io


@patch('builtins.input', side_effect=['2', 'Alice', '85', '90', 'Bob', '55', '60'])
@patch('sys.stdout', new_callable=io.StringIO)
def test_student_grades(mock_stdout, mock_input):
    import Question5
    
    # Check the output
    output = mock_stdout.getvalue()
    
    assert "Enter data for student 1:" in output
    assert "Alice: A" in output
    assert "Enter data for student 2:" in output
    assert "Bob: C" in output
