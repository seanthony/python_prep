import disk
import core


def get_username(user_dictionary):
    ''' {str: int} -> str 
    prints out the valid usernames
    and returns the user selected
    username if valid
    '''
    print('Usernames:', ', '.join(user_dictionary.keys()))
    while True:
        username = input('Which user? ')
        if username in user_dictionary.keys():
            return username
        else:
            print(username, 'is an invalid option.')


def get_hours():
    ''' None -> int
    returns a valid number of hours given by the user
    '''
    while True:
        hours = input('How many hours? ')
        if hours.isdigit():
            return int(hours)
        print('invalid entry!')


def main():
    roster_raw_info = disk.open_file('./roster.txt')
    user_dictionary = core.create_user_dictionary(roster_raw_info)
    username = get_username(user_dictionary)
    hours = get_hours()
    core.add_hours(user_dictionary, username, hours)


if __name__ == '__main__':
    main()
