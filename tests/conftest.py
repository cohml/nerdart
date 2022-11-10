import numpy as np
import pytest


@pytest.fixture(scope="module")
def array():
    return np.linspace(0, 1)
