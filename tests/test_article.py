import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_creation_and_save():
    author = Author("Malcolm Gladwell")
    magazine = Magazine("The Thinker", "Philosophy")
    author.save()
    magazine.save()

    article = Article("Blink and You Miss It", author.id, magazine.id)
    article.save()

    assert article.id is not None

def test_article_belongs_to_author_and_magazine():
    author = Author("Zadie Smith")
    magazine = Magazine("Cultural Digest", "Culture")
    author.save()
    magazine.save()

    article = Article("Race and Representation", author.id, magazine.id)
    article.save()

    assert article.author_id == author.id
    assert article.magazine_id == magazine.id
