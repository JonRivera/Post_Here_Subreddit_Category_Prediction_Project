from fastapi.testclient import TestClient
import pickle
from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return whether Test Post is returning the proper subreddits."""
    response = client.post(
        '/predict',
        json={
            "Title": "This is a Reddit title",
            "Post": "This is a Redd post"
        }
    )
    with open("models/mvp_log_pipe", "rb") as file:
        model = pickle.load(file)

    assert model.predict(['Something'])[0] in model.classes_
    body = response.json()
    assert response.status_code == 200
    # assert body['prediction'] == ["HailCorporate", "bestoflegaladvice",
    #                               "KarmaCourt", "boringdystopia", "pcmasterrace"]
    # 'a' in ['a', 'b', 'c']
    # the model has an attribute
    # so if oyu said prediction in model.classes_
    assert body == {'prediction': ["HailCorporate", "bestoflegaladvice",
                                   "KarmaCourt", "boringdystopia", "pcmasterrace"]}


def test_invalid_input():
    """Return when test_post Title is empty."""
    response = client.post(
        '/predict',
        json={
            "Text": "",
            "Post": [3, 5, 8]
        }
    )
    body = response.json()
    # assert Post == str???
    assert response.status_code == 200
    assert body['prediction'] == ["boringdystopia", "pcmasterrace",
                                  "worldnews", "britishproblems", "bestoflegaladvice"]
    # but ^ would be correct and we want to test invalid input
