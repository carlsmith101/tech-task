import requests

BASE_URL = "https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/"

# valid requests

def get(article_id):
    return requests.get('{}/{}'.format(BASE_URL, article_id))

def get_all():
    return requests.get(BASE_URL)

def put(article_id):
    return requests.put(url='{}{}'.format(BASE_URL, article_id), data={'title':'Test'})

def post():
    return requests.post(url=BASE_URL, data={'title':'Test'})

def delete(article_id):
    return requests.delete(url='{}{}'.format(BASE_URL, article_id))

# invalid requests

def post_single(article_id):
    return requests.post('{}{}'.format(BASE_URL, article_id))

def put_all():
    return requests.put(BASE_URL)

def delete_all():
    return requests.delete(BASE_URL)