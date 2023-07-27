from apikey.article.models import Article


def create_article(title, body):
    return Article.objects.create(title=title, body=body)