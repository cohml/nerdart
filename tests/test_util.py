import numpy as np

from nerdart.utils import get_artwork_paths, xy


def test_get_artwork_paths():
    computed_artwork_paths = get_artwork_paths()
    assert len(computed_artwork_paths) == 45
    assert computed_artwork_paths[0].stem == "unnamed"
    assert computed_artwork_paths[-1].stem == "smoke"


def test_xy(array):
    x_computed, y_computed = xy(array)
    x_expected = np.sin(array)
    np.testing.assert_array_equal(x_computed, x_expected)
    y_expected = np.cos(array)
    np.testing.assert_array_equal(y_computed, y_expected)
