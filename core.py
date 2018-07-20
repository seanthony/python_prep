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


def get_most_hours(user_dictionary):
    ''' {str: int} -> [str]
    returns a list of the username with the most hours
    will return multiple names if the same
    '''
    max_hours = max(user_dictionary.values())
    users = []
    for user in user_dictionary.keys():
        if user_dictionary.get(user) == max_hours:
            users.append(user)
    return users
