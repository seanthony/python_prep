def create_user_dictionary(user_list):
    user_dictionary = {}
    for user_info in user_list:
        items = user_info.split(',')
        key = items[0].strip()
        value = int(items[1].strip())
        user_dictionary[key] = value
    return user_dictionary


def add_hours(user_dictionary, username, hours):
    ''' ({str: int}, str, int) -> None
    updates user_dictionary with an increase in hours
    '''
    user_dictionary[username] += hours


def create_file_string(user_dictionary):
    ''' {str: int} -> str
    turns the user_dictionary into a string
    '''
    file_string = 'name, hours'
    for name, hours in user_dictionary.items():
        file_string += '\n{}, {}'.format(name, hours)
    return file_string
