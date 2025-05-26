from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_creation_and_articles():
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    article = Article("Test Article", author.id, magazine.id)
    article.save()

    articles = author.articles()
    assert any(a["title"] == "Test Article" for a in articles)

def test_author_magazines():
    author = Author("Multi Mag Author")
    author.save()
    m1 = Magazine("Mag One", "Cat One")
    m2 = Magazine("Mag Two", "Cat Two")
    m1.save()
    m2.save()
    Article("A1", author.id, m1.id).save()
    Article("A2", author.id, m2.id).save()
    mags = author.magazines()
    assert len(mags) == 2
