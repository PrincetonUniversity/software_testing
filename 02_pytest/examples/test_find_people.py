"""software_testing/03_unittest/examples/test_find_people.py"""
# pylint: disable=W0621,W0613
import pytest
import find_people
import mock_data


@pytest.fixture()
def setup():
    """Set up and clean up test data"""
    mock_dir = mock_data.generate_test_data()
    find_people.GPFS_FOLDER = mock_dir
    yield
    mock_data.delete_temp_directory(mock_dir)


def test_legal_zipcode(setup):
    """Test finding people using zip code."""
    people = find_people.find_people("10036")
    assert len(people) == 1


def test_multiple_results(setup):
    """Test finding multiple people in same zip code."""
    people = find_people.find_people("10019")
    assert len(people) == 2


def test_no_results(setup):
    """Test search on zip code with no result."""
    people = find_people.find_people("00000")
    assert len(people) == 0


if __name__ == "__main__":
    pytest.main([__file__])
