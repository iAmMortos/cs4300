
import context
import task7
import numpy as np
import pytest


def test_multiply_matrices():
  m1 = np.array([[1, 2, 3]])
  m2 = np.transpose(np.array([[4, 5, 6]]))
  m3 = task7.multiply_matrices(m1, m2)
  assert m3.shape == (3, 3)
  assert np.array_equal(m3, np.array([[4, 8, 12],
                                      [5, 10, 15],
                                      [6, 12, 18]]))


def test_dot_product():
  m1 = np.array([[1, 2, 3]])  # 3x1
  m2 = np.transpose(np.array([[4, 5, 6]]))  # 1x3
  m3 = task7.dot_product(m1, m2)  # 1x1
  assert m3.shape == (1, 1)
  assert m3[0][0] == 32

  m4 = task7.dot_product(m2, m1)  # 3x3
  assert m4.shape == (3, 3)
  assert np.array_equal(m4, np.array([[4, 8, 12],
                                      [5, 10, 15],
                                      [6, 12, 18]]))

  m5 = np.array([[1, 2], [3, 4]]) # 2x2

  with pytest.raises(ValueError):
    task7.dot_product(m5, m4) # 2x2 matrix dotted with 3x3 (impossible)
