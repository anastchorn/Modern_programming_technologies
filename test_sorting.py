from sorting import sort_list
import pytest


def test_sort_list():
#Тести для перевірки коректності функції сортування
    assert sort_list([3, 2, 1]) == [1, 2, 3], "Помилка"
    assert sort_list([5, -1, 0]) == [-1, 0, 5], "- числа"
    assert sort_list([]) == [], "Порожній список)"
    assert sort_list([1]) == [1], "Список з 1"
    assert sort_list([1, 1, 1]) == [1, 1, 1], "Однакові елементи"
