import math
from unittest.mock import patch
import pytest
import importlib

def test_garden_requirements(capfd):
  # Patch input to simulate user input
  inputs = iter([16, 2, 1, 0.5])
  
  with patch('builtins.input', lambda _: next(inputs)):
      import Question1

  # Capture printed output
  out, _ = capfd.readouterr()

  # Split the output lines and strip any extra spaces
  output_lines = [line.strip() for line in out.split('\n') if line.strip()]

  # Assertions on printed values
  assert "Plants for each semicircle garden: 6" in output_lines
  assert "Plants for the circle garden: 12" in output_lines
  assert "Total plants for garden: 36" in output_lines
  assert "Soil for each semicircle garden: 0.9 cubic yards" in output_lines
  assert "Soil for the circle garden: 1.9 cubic yards" in output_lines
  assert "Total soil for the garden: 5.6 cubic yards" in output_lines
  assert "Total fill for the garden: 1.9 cubic yards" in output_lines

def test_small_garden_requirements(capfd):
  import Question1
  # Patch input to simulate user input
  inputs = iter([8, 1.5, 0.5, 0.25])

  with patch('builtins.input', lambda _: next(inputs)):
      import Question1
      importlib.reload(Question1)

  # Capture printed output
  out, _ = capfd.readouterr()

  # Split the output lines and strip any extra spaces
  output_lines = [line.strip() for line in out.split('\n') if line.strip()]

  # Assertions on printed values
  assert "Plants for each semicircle garden: 2" in output_lines
  assert "Plants for the circle garden: 5" in output_lines
  assert "Total plants for garden: 13" in output_lines
  assert "Soil for each semicircle garden: 0.1 cubic yards" in output_lines
  assert "Soil for the circle garden: 0.2 cubic yards" in output_lines
  assert "Total soil for the garden: 0.7 cubic yards" in output_lines
  assert "Total fill for the garden: 0.2 cubic yards" in output_lines
