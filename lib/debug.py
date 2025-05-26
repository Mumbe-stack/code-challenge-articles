from lib.models.author import Author

if __name__ == "__main__":
    author = Author.find_by_id(1)
    print(f"Author: {author.name}")
    print("Articles:", [a["title"] for a in author.articles()])
    print("Magazines:", [m["name"] for m in author.magazines()])
