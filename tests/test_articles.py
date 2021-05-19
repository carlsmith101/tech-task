import calls.articles as articles

# valid requests

def test_get_all_articles_status_code_is_200():
    response = articles.get_all()
    assert response.status_code == 200

def test_get_all_articles_content_type_is_json():
    response = articles.get_all()
    assert response.headers["Content-Type"] == 'application/json'

def test_get_all_articles_response_is_correct_structure():
    response = articles.get_all()
    for article in response.json():
        assert_article_structure(article)

def test_get_single_article_status_code_is_200():
    response = articles.get(1)
    assert response.status_code == 200

def test_get_single_article_content_type_is_json():
    response = articles.get(1)
    assert response.headers["Content-Type"] == 'application/json'

def test_get_single_article_response_is_correct_structure():
    response = articles.get(1)
    assert_article_structure(response.json())

def test_get_missing_article_status_code_is_404():
    response = articles.get(6)
    assert response.status_code == 404 and response.text == '"Not found"'

# valid requests, endpoints disabled

def test_attempt_post_article_status_code_is_404():
    response = articles.post()
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'

def test_attempt_put_article_status_code_is_404():
    response = articles.put(1)
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'

def test_attempt_delete_article_status_code_is_404():
    response = articles.delete(1)
    assert response.status_code == 404 and response.text == '"Endpoint disabled"'

# invalid requests - instructions suggest these should return 404 - actually return 400

def test_attempt_post_single_article_status_code_is_400():
    response = articles.post_single(1)
    assert response.status_code == 400 and response.text == '{"msg":"Invalid request"}'

def test_attempt_put_all_articles_status_code_is_400():
    response = articles.put_all()
    assert response.status_code == 400 and response.text == '{"msg":"Invalid request"}'

def test_attempt_delete_all_articles_status_code_is_400():
    response = articles.delete_all()
    assert response.status_code == 400 and response.text == '{"msg":"Invalid request"}'

# helper methods

def assert_article_structure(article):
    assert int(article["id"]) > 0
    assert isinstance(article["createdAt"], str) and article["createdAt"] != ""
    assert isinstance(article["title"], str) and article["title"] != ""
    assert isinstance(article["sensitive"], bool)
    assert isinstance(article["topics"], list)
    assert "image" in article
    assert isinstance(article["priority"], int)