import requests

BASE_URL = "https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/"

# base

def test_valid_GET_articles_status_code_is_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_POST_article_status_code_is_404():
    response = requests.post(url=BASE_URL, data='')
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'

# child

def test_GET_article_status_code_is_200():
    response = requests.get(BASE_URL + "1")
    assert response.status_code == 200

def test_PUT_article_status_code_is_404():
    response = requests.put(url=BASE_URL + "1", data='')
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'

def test_DELETE_article_status_code_is_404():
    response = requests.delete(BASE_URL + "1")
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'