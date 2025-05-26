from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_data():
    a1 = Author("Chinua Achebe")
    a1.save()
    a2 = Author("Ngũgĩ wa Thiong’o")
    a2.save()

    m1 = Magazine("African Writers", "Literature")
    m2 = Magazine("East African Times", "Politics")
    m1.save()
    m2.save()

    Article("The Rise of the African Novel", a1.id, m1.id).save()
    Article("Language and Freedom", a2.id, m2.id).save()
    Article("Tribalism in Politics", a1.id, m2.id).save()

    print("Seeding complete.")

if __name__ == "__main__":
    seed_data()
