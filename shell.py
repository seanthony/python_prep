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


def main():
    roster_raw_info = disk.open_file('./roster.txt')
    user_dictionary = core.create_user_dictionary(roster_raw_info)
    username = get_username(user_dictionary)


if __name__ == '__main__':
    main()
