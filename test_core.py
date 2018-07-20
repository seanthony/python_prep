from core import *


def test_create_user_dictionary():
    user_dictionary = create_user_dictionary(
        ['Sean, 0\n', 'Nate, 0\n', 'Evil Nate, 0\n'])
    assert user_dictionary == {'Sean': 0, 'Nate': 0, 'Evil Nate': 0}


def test_add_hours():
    user_dictionary = {'Sean': 0, 'Nate': 0, 'Evil Nate': 0}
    username = 'Sean'
    hours = 10
    add_hours(user_dictionary, username, hours)
    assert user_dictionary == {'Sean': 10, 'Nate': 0, 'Evil Nate': 0}


def test_create_file_string():
    user_dictionary = {'Sean': 10}
    file_string = create_file_string(user_dictionary)
    assert file_string == 'name, hours\nSean, 10'


def test_get_most_hours_one():
    user_dictionary = {'Sean': 10, 'Nate': 0, 'Evil Nate': 0}
    username = get_most_hours(user_dictionary)
    assert username == ['Sean']


def test_get_most_hours_multiple():
    user_dictionary = {'Sean': 10, 'Nate': 10, 'Evil Nate': 10}
    username = get_most_hours(user_dictionary)
    sorted(username)
    assert username == ['Evil Nate', 'Nate', 'Sean']
