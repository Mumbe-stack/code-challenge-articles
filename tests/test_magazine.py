import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article

def test_magazine_creation_and_save():
    mag = Magazine("Science Today", "Science")
    mag.save()
    fetched = Magazine.find_by_id(mag.id)
    assert fetched.name == "Science Today"
    assert fetched.category == "Science"

def test_magazine_articles():
    mag = Magazine("Tech World", "Technology")
    mag.save()
    author = Author("Ada Lovelace")
    author.save()
    Article("AI Revolution", author.id, mag.id).save()
    Article("Future of Coding", author.id, mag.id).save()

    articles = mag.articles()
    titles = [a["title"] for a in articles]
    assert "AI Revolution" in titles
    assert "Future of Coding" in titles

def test_magazine_contributors():
    mag = Magazine("Writers Digest", "Literature")
    mag.save()
    a1 = Author("George Orwell")
    a2 = Author("Virginia Woolf")
    a1.save()
    a2.save()
    Article("Dystopia", a1.id, mag.id).save()
    Article("Modern Fiction", a2.id, mag.id).save()

    contributors = mag.contributors()
    names = [c["name"] for c in contributors]
    assert "George Orwell" in names
    assert "Virginia Woolf" in names
