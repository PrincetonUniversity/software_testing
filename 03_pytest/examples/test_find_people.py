import pytest
import find_people
import mock_data

@pytest.fixture(autouse=True)
def setUp():
    mock_dir = mock_data.generate_test_data()
    find_people.GPFS_FOLDER = mock_dir
    yield
    mock_data.delete_temp_directory(mock_dir)

def test_legal_zipcode():
    people = find_people.find_people("10036")
    assert len(people) == 1

def test_multiple_results():
    people = find_people.find_people("10019")
    assert len(people) == 2

def test_no_results():
    people = find_people.find_people("00000")
    assert len(people) == 0
