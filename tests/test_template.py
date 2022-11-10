import pytest

from nerdart import DEFAULTS, Template


def test_template_generate_exists():
    name = "smoke"
    expected_error_msg = "Artwork already exists"
    with pytest.raises(FileExistsError, match=expected_error_msg):
        Template(name).generate()


def test_template_generate_not_exist():
    name = "foo"
    expected_filepath = DEFAULTS["ART_DIR"] / f"{name}.py"
    assert (
        not expected_filepath.exists()
    ), f"Remove test file before running test: {expected_filepath}"
    try:
        Template(name).generate()
        assert expected_filepath.exists()
        assert len(expected_filepath.read_text()) == 573
    finally:
        pass
        expected_filepath.unlink()