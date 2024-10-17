"""Verify that functions found in names.py work correctly"""

from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """
    Verify that the make_full_name function works correctly.
    Parameters:
        None
    Return:
        Nothing
    """
    # Call the make_full_name function and verify that it returns a string.
    full_name = make_full_name("Sally", "Brown")
    assert isinstance(full_name, str), "make_full_name function must return a string"

    # Call the make_full_name function three times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.
    assert make_full_name("", "") == "; "
    assert make_full_name("Abraham", "Lincoln") == "Lincoln; Abraham"
    assert make_full_name("Iris", "West-Allen") == "West-Allen; Iris"


def test_extract_family_name():
    """
    Verify that the extract_family_name function works correctly.
    Parameters:
        None
    Return:
        Nothing
    """
    # Call the extract_family_name function and verify that it returns a string.
    family_name = extract_family_name("Brown; Sally")
    assert isinstance(
        family_name, str
    ), "extract_family_name function must return a string"

    # Call the extract_family_name function three times and use an assert
    # statement to verify that the string returned by the
    # extract_family_name function is correct each time.
    assert extract_family_name("; ") == ""
    assert extract_family_name("Adams; John") == "Adams"
    assert extract_family_name("Day-Lewis; Daniel") == "Day-Lewis"


def test_extract_given_name():
    """
    Verify that the extract_given_name function works correctly.
    Parameters:
        None
    Return:
        Nothing
    """
    # Call the extract_given_name function and verify that it returns a string.
    given_name = extract_given_name("Brown; Sally")
    assert isinstance(
        given_name, str
    ), "extract_given_name function must return a string"

    # Call the extract_given_name function three times and use an assert
    # statement to verify that the string returned by the
    # extract_given_name function is correct each time.
    assert extract_given_name("; ") == ""
    assert extract_given_name("Brady; Tom") == "Tom"
    assert extract_given_name("Gordon-Levitt; Joseph") == "Joseph"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
