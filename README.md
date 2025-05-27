# Phase 3 Code Challenge: Articles - Without SQLAlchemy
# Description
This project models a content publishing system using Python classes and raw SQL. It establishes relationships between authors, articles, and magazines, and provides methods to interact with a SQLite database—without using SQLAlchemy.

The relationships modeled are:
    An Author can write many Articles
    A Magazine can publish many Articles
    An Article belongs to both an Author and a Magazine
    This creates a many-to-many relationship between Authors and Magazines

# Project Structure
code-challenge-articles/
├── Pipfile / Pipfile.lock          # Pipenv environment & dependencies
├── .gitignore                      # Ignore files like DB and __pycache__
├── README.md                       # Project documentation
├── articles.db                     # SQLite database (created after setup)
│
├── lib/
│   ├── __init__.py
│   ├── debug.py                    # Interactive testing
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py           # Handles DB connection
│   │   ├── schema.sql              # Table definitions
│   │   └── seed.py                 # Sample data seeding
│   └── models/
│       ├── __init__.py
│       ├── author.py               # Author model
│       ├── magazine.py             # Magazine model
│       └── article.py              # Article model
│
├── scripts/
│   └── setup_db.py                 # Loads schema into the DB
│
└── tests/
    ├── __init__.py
    ├── test_author.py              # Author tests
    ├── test_article.py             # Article tests
    └── test_magazine.py 


# Setup Instructions
1. Clone the Repository
git clone (https://github.com/Mumbe-stack/code-challenge-articles)
cd code-challenge-articles

2. Install Dependencies Using Pipenv
pipenv install
pipenv shell

3. Initialize the Database
python -m scripts.setup_db

# Running Tests
pytest (All tests for authors, magazines, and articles will run automatically.)

#  Features
Create, find, and update Authors, Magazines, and Articles
Link articles to both authors and magazines
Query all articles by an author
Query all magazines an author has written for
List all contributors to a magazine
Cleanly structured raw SQL logic inside Python OOP classes
Handles database transactions and basic validation

# Technologies Used
Python 3.8+
SQLite (via sqlite3)
Pipenv
Pytest

# Developer Utilities
Interactive Debugging
You can test logic directly using:
    python lib/debug.py

# Author
Mercy Mumbe(https://github.com/Mumbe-stack)

