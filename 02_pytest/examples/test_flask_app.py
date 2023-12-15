"""Unit test for the flask_app."""
import flask
import flask_app


def test_lookup_id(mocker):
    """Test look up of question id '3'."""

    class MockRequest:
        def __init__(self):
            self.args = {"id": "3"}

    flask.request = MockRequest()

    def mock_response(content, status=200):
        assert status == 200
        assert "How many dwarfs are not happy" in str(content)
        assert "6" in str(content)

    mocker.patch("flask.Response", side_effect=mock_response)
    flask.request = MockRequest()
    flask_app.get_questions()


def test_id_not_found(mocker):
    """Test lookup of id not found."""

    class MockRequest:
        def __init__(self):
            self.args = {"id": "illegal"}

    flask.request = MockRequest()

    def mock_response(content, status):
        assert content == "The id 'illegal' not found."
        assert status == 400

    mocker.patch("flask.Response", side_effect=mock_response)
    flask.request = MockRequest()
    flask_app.get_questions()
