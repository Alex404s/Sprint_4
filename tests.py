import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
      
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['','Количество символов, которое должно быть больше сорока символов'])
    def test_add_new_book_incorrect_name_empty_list(self, collector_1, name):
        
        collector_1.add_new_book(name)
                
        assert len(collector_1.get_books_genre()) == 0


    def test_add_new_book_repeat_name_one_book_in_list(self, collector_2):
              
        collector_2.add_new_book('Овод')
        collector_2.add_new_book('Овод')

        assert len(collector_2.get_books_genre()) == 1


    def test_set_book_genre_set_one_genre(self, collector_3):
       
        collector_3.add_new_book('Аленький цветочек') 
        collector_3.set_book_genre('Аленький цветочек', 'Мультфильмы')

        assert collector_3.get_book_genre('Аленький цветочек') == 'Мультфильмы'
    
    
    def test_get_book_genre_no_added_genre_empty_genre(self, collector_4):
        
        collector_4.add_new_book('Подводная братва')
        
        assert collector_4.get_book_genre('Подводная братва') == ''

    
    def test_get_books_with_specific_genre_add_two_books_fantastic(self, collector_5):
        
        collector_5.add_new_book('Автостопом по галактике')
        collector_5.add_new_book('Война миров')
        collector_5.set_book_genre('Автостопом по галактике', 'Фантастика')
        collector_5.set_book_genre('Война миров', 'Фантастика')

        assert collector_5.get_books_with_specific_genre('Фантастика') == ['Автостопом по галактике','Война миров']


    @pytest.mark.parametrize('name, genre', [['Война мирвВойна мирвВойна мирвВойна мирв' , 'Фантастика'],
                                             ['Ч' , 'Ужасы'],
                                             ['Евангелион' , 'Мультфильмы']])
    def test_get_books_genre_view_three_books_with_genre(self, collector_6, name, genre):
        
        collector_6.add_new_book(name)
        collector_6.set_book_genre(name, genre)

        assert collector_6.get_books_genre() == {name: genre}


    @pytest.mark.parametrize('name, genre', [['Незнайка' , 'Фантастика'],
                                             ['Мулан' , 'Мультфильмы'],
                                             ['День сурка' , 'Комедии']])
    def test_get_books_for_children_add_fantastic_cartoon_comedy_books(self, collector_7, name, genre):
        
        collector_7.add_new_book(name)
        collector_7.set_book_genre(name, genre)

        assert collector_7.get_books_for_children() == [name]

    
    def test_add_book_in_favorites_add_one_book(self,collector_8):
        
        collector_8.add_new_book('Пролетая над гнездом кукушки')
        collector_8.add_book_in_favorites('Пролетая над гнездом кукушки')

        assert collector_8.get_list_of_favorites_books() == ['Пролетая над гнездом кукушки']


    def test_delete_book_from_favorites_delete_one_book_empty_favorites(self, collector_9):
        
        collector_9.add_new_book('Дюна')
        collector_9.add_book_in_favorites('Дюна')
        collector_9.delete_book_from_favorites('Дюна')

        assert collector_9.get_list_of_favorites_books() == []

    
    def test_get_list_of_favorites_books_default_empty(self, collector_10):
        
        assert collector_10.get_list_of_favorites_books() == []
