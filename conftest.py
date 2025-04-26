import pytest
from main import BooksCollector

@pytest.fixture
def empty_collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    books = {
        "Война и мир": "Фантастика",
        "Метро 2033": "Фантастика",
        "Шерлок Холмс": "Детективы",
        "Ночной дозор": "Ужасы",
        "Трое в лодке": "Комедии",
        "Корпорация монстров": "Мультфильмы"
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def collector_with_favorites():
    collector = BooksCollector()
    favorites = ["Мастер и Маргарита", "1984", "Тихий Дон"]
    for name in favorites:
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
    return collector