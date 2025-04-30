import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1. Тест для add_new_book
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Тест для set_book_genre с параметризацией
    @pytest.mark.parametrize("genre, expected", [
        ("Фантастика", "Фантастика"),
        ("Ужасы", "Ужасы"),
        ("Роман", ""),
        ("", "")
    ])
    def test_set_book_genre(self, empty_collector, genre, expected):
        empty_collector.add_new_book("1984")
        empty_collector.set_book_genre("1984", genre)
        assert empty_collector.get_book_genre("1984") == expected

    # 3. Тест для get_books_with_specific_genre
    @pytest.mark.parametrize("genre, expected_count", [
        ("Фантастика", 2),
        ("Детективы", 1),
        ("Мультфильмы", 1)
    ])
    def test_get_books_with_specific_genre(self, collector_with_books, genre, expected_count):
        assert len(collector_with_books.get_books_with_specific_genre(genre)) == expected_count

    # 4. Тест для get_books_for_children
    def test_get_books_for_children(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert "Трое в лодке" in children_books
        assert "Корпорация монстров" in children_books
        assert "Ночной дозор" not in children_books

    # 5. Тесты для работы с избранным
    def test_add_and_remove_favorites(self, empty_collector):
        # Добавление
        empty_collector.add_new_book("Мастер и Маргарита")
        empty_collector.add_book_in_favorites("Мастер и Маргарита")
        assert "Мастер и Маргарита" in empty_collector.get_list_of_favorites_books()

        # Удаление
        empty_collector.delete_book_from_favorites("Мастер и Маргарита")
        assert "Мастер и Маргарита" not in empty_collector.get_list_of_favorites_books()

    # 6. Тест для несуществующей книги в избранном
    def test_add_non_existing_book_to_favorites(self, empty_collector):
        empty_collector.add_book_in_favorites("Несуществующая книга")
        assert len(empty_collector.get_list_of_favorites_books()) == 0

    # 7. Тест структуры books_genre
    def test_get_books_genre_returns_correct_structure(self, empty_collector):
        empty_collector.add_new_book("Книга")
        assert empty_collector.get_books_genre() == {"Книга": ""}

    # 8. Тест начального состояния
    def test_initial_state(self, empty_collector):
        assert empty_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert empty_collector.genre_age_rating == ['Ужасы', 'Детективы']
        assert len(empty_collector.get_books_genre()) == 0

    # 9. Тест пустого жанра у новой книги
    def test_new_book_has_empty_genre(self, empty_collector):
        empty_collector.add_new_book("Тихий Дон")
        assert empty_collector.get_book_genre("Тихий Дон") == ""

    # 10. Тест для get_list_of_favorites_books с несколькими книгами
    def test_get_list_of_favorites_books_return_correct_books(self,collector_with_favorites):
        favorites = collector_with_favorites.get_list_of_favorites_books()
        assert len(favorites) == 3
        assert set(favorites) == {"Мастер и Маргарита", "1984", "Тихий Дон"}

    # 11. Тест для пустого списка избранного
    def test_get_list_of_favorites_books_empty_list(self,empty_collector):
        assert empty_collector.get_list_of_favorites_books() == []


