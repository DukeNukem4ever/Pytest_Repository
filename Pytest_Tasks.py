import pytest


# Часть 1: структуры данных str

# Тест 1: перевод строки в верхний регистр

def test_to_upper():
    assert "котик".upper() == "КОТИК"


# Тест 2: первая буква строки

def test_first_letter():
    assert "Радуга"[0] == "Р"


# Тест 3: сложение строк

@pytest.mark.parametrize("elem1,elem2",
                         [("\"a\" + 4", "a4")])
def test_add_strings(elem1, elem2):
    try:
        assert eval(elem1) == elem2
    except TypeError:
        pass


# Часть 2: структуры данных list

# Тест 1: удаление элемента из списка

def test_remove_from_list():
    try:
        assert [].remove("Ничего") is None
    except ValueError:
        pass


# Тест 2: последний элемент списка

def test_get_last_element():
    assert ['1', '2', '3', '4', '5'][-1] == '5'


# Тест 3: длина списка


@pytest.mark.parametrize("lisst, result",
                         [("len([\"a\", \"b\", \"c\", \"d\", \"e\"])", 5)])
def test_find_numbers(lisst, result):
    assert eval(lisst) == result
