"""Flask REST web server application used to demonstrate unit testing."""
import flask

app = flask.Flask(__name__)


@app.route("/questions", methods=["GET"])
def get_questions() -> flask.Response:
    """
    API route that returns a list of questions and answers.
    Parameters:
        id:     A question ID.
    Returns:
        An array of dict with attributes: id, question, answer.

    If the id parameter is specified then only return the question with that id.
    """
    try:
        questions = [
            {
                "id": "1",
                "question": "What city is the capital of the US (in 1783)?",
                "answer": "princeton",
            },
            {
                "id": "2",
                "question": "What kind of magic do cows believe in?",
                "answer": "MOODOO",
            },
            {"id": "3", "question": "How many dwarfs are not happy?", "answer": "6"},
        ]
        query_parameters = flask.request.args
        query_id = query_parameters.get("id") if query_parameters else None
        if query_id is not None:
            result = None
            for entry in questions:
                if entry.get("id") == query_id:
                    result = [entry]
            if result is None:
                raise ValueError(f"The id '{query_id}' not found.")
        else:
            result = questions
        return flask.Response(result)
    except Exception as e:
        return flask.Response(str(e), status=400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
