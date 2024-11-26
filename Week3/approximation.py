from pytest import approx
import pytest

assert 2.09 == approx(2.088, abs=0.001)
print('worked')