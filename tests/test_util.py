import numpy as np
import pytest

from pathlib import Path

from nerdart.utils import get_artwork_paths, is_artwork, xy


def test_get_artwork_paths():
    computed_artwork_paths = list(get_artwork_paths())
    error_msg = "Have you committed all new artworks?"
    assert len(computed_artwork_paths) == 45, error_msg
    error_msg += " This test relies on the alphabetical order of artwork names."
    assert computed_artwork_paths[0].stem == "unnamed", error_msg
    assert computed_artwork_paths[-1].stem == "smoke", error_msg


@pytest.mark.parametrize(
    "expected_output,filename",
    [
        (False, "__init__.py"),
        (False, "__init__"),
        (True, "init"),
        (False, "_null-ls_922254_foo.py"),
        (False, "_null-ls_922254_foo"),
        (True, "null-ls_922254_foo"),
        (True, "angular.py"),
    ],
)
def test_is_artwork(expected_output, filename):
    path = Path(filename)
    computed_output = is_artwork(path)
    assert computed_output == expected_output


def test_xy(array):
    x_computed, y_computed = xy(array)
    x_expected = np.sin(array)
    np.testing.assert_array_equal(x_computed, x_expected)
    y_expected = np.cos(array)
    np.testing.assert_array_equal(y_computed, y_expected)
