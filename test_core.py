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
